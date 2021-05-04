"""This module contains Web Client for Data Aggregator"""
import os
import sys
import time
import csv
import logging
from datetime import datetime

from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import PATH_TO_METAMASK_EXTENSION_CRX_FILE, TIMEOUT_FOR_CONTRACTS_PAGE_LOADING, TIMEOUT_FOR_VERBOSE_PAGE_LOADING, \
    TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING, REDUCED_TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING, PASSWORD_FOR_METAMASK, \
    HEADERS, BORDER_PHRASE, TOTAL_STAKED, APPEND_MODE, DISCLAIMER, NUMBER_OF_REFRESH_TRIES

from parsers import extract_contract_values

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)


class VfatCrauler:
    """A class to perform vfat site crawling"""

    def __init__(self, address, page_name, various_links_to_run=None):
        self._page_name = page_name
        self._file_name = f"results/{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}_{page_name}.csv" 
        
        self._various_links_to_run = various_links_to_run

        options = Options()
        options.add_extension(os.path.join(ROOT_DIR, PATH_TO_METAMASK_EXTENSION_CRX_FILE))
        options.add_argument(
            f"user-data-dir=EXTENSION_CONFIG_{page_name}")  # file to save metamask extensions parameters

        self._address = address
        self._authorize = False

        self._browser = webdriver.Chrome(options=options)
        self._page = self._browser.current_window_handle

        self._make_csv_file_ready()

        self._not_pulled_various_links = []
        self._partially_pulled_various_links = []
        self._not_parsed_links = []

    def _make_csv_file_ready(self):
        with open(self._file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)

    def _authorize_in_site(self):
        try:
            popup_pages = self._browser.window_handles
            self._browser.switch_to.window(popup_pages[0])
            time.sleep(REDUCED_TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING)
            user_password_page = WebDriverWait(self._browser,
                                               TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING).until(
                EC.presence_of_element_located((By.XPATH, ".//*[@id='password']")))

            user_password_page.send_keys(PASSWORD_FOR_METAMASK)

            WebDriverWait(self._browser,
                          TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'MuiButton-label'))).click()

            self._browser.close()
            self._authorize = True
            logging.info(f'Address = {self._address}. Metamask authorization was accessed')

        except Exception as exc:
            logging.error(f'Address = {self._address}. '
                          f'Please restart the script. Cant authorize in Metamask: {exc}')

    def _catch_contracts_table(self, various_link):
        self._browser.maximize_window()

        for i in range(NUMBER_OF_REFRESH_TRIES):
            try:
                WebDriverWait(self._browser, TIMEOUT_FOR_CONTRACTS_PAGE_LOADING).until(
                    EC.text_to_be_present_in_element((By.ID, 'log'), TOTAL_STAKED))

                return self._browser.find_element_by_id('log')

            except:
                if i != NUMBER_OF_REFRESH_TRIES - 1:
                    self._browser.refresh()
                    logging.warning(f'Address={self._address}. '
                                    f'Page by various link = {various_link} was not fully loaded, page is refreshing ')
        else:
            logging.warning(f'Address={self._address}. '
                            f'Page by various link = {various_link} was not fully loaded, but '
                            f'was parsed anyway')
            self._partially_pulled_various_links.append(various_link)
            return self._browser.find_element_by_id('log')

    def _parse_contracts(self, contracts, various_name, various_link):
        starting_index = contracts.find(BORDER_PHRASE)
        contracts = contracts[starting_index + len(BORDER_PHRASE):]

        ending_index = contracts.find('\n' + TOTAL_STAKED)
        if ending_index != -1:
            contracts = contracts[:ending_index]

        contracts = contracts[starting_index + len(BORDER_PHRASE):]

        contracts = contracts.split('\n\n')

        added = False
        for contract in contracts:
            name_1, name_2, contract_apr, contract_staked = extract_contract_values(contract,
                                                                                    self._address,
                                                                                    various_link)
            if name_1 is None:
                continue

            row_to_write = [self._page_name, various_name, name_1, name_2, contract_apr, contract_staked]
            with open(self._file_name, APPEND_MODE) as file:
                writer = csv.writer(file)
                writer.writerow(row_to_write)
                added = True
        if not added:
            self._not_parsed_links.append(various_link)



    def _parse_various_links(self, various_pages):
        return [v.get_attribute('href') for v in various_pages]

    def _load_contracts(self):
        try:
            self._browser.switch_to.window(self._page)
            self._browser.get(self._address)

            WebDriverWait(self._browser, TIMEOUT_FOR_VERBOSE_PAGE_LOADING).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, 'container'), DISCLAIMER))

            self._browser.maximize_window()
            logging.info(f'Address = {self._address}. '
                         f'Page with various links was successfully loaded')

        except Exception as exc:
            logging.error(f'Address = {self._address}. Please restart script. '
                          f'Page with various links was not loaded: {exc}')
            self._browser.quit()

        for i in range(NUMBER_OF_REFRESH_TRIES):
            try:
                various_pages = WebDriverWait(self._browser, TIMEOUT_FOR_CONTRACTS_PAGE_LOADING).until(
                    EC.presence_of_all_elements_located((By.LINK_TEXT, 'Various')))
                break
            except:
                self._browser.refresh()
                logging.error(
                    f'Address = {self._address}. Page with various links is unavailable. Trying to reconnect.')
        else:
            logging.error(f'Address = {self._address}. Please restart script. '
                          f'Did not catch any various links, page is unavailable')
            self._browser.quit()
            return

        various_links = self._various_links_to_run if self._various_links_to_run else self._parse_various_links(various_pages)
        for various_link in tqdm(various_links, desc='Iterating various links'):
            various_name = os.path.basename(os.path.normpath(various_link))

            print(f"Opening {various_name} at {various_link}")
            try:
                self._browser.execute_script(f"window.open('{various_link}','_blank')")
                self._browser.switch_to.window(self._browser.window_handles[-1])
            except:
                logging.warning(f'Address={self._address}. '
                                f'Did not catch any contracts from various link {various_link}')
                self._not_pulled_various_links.append(various_link)
                continue

            contracts_table = self._catch_contracts_table(various_link)

            if contracts_table is not None:
                contracts = contracts_table.text
            else:
                logging.warning(f'Address={self._address}. '
                                f'Did not catch any contracts from various link {various_link}')
                self._not_pulled_various_links.append(various_link)
                continue

            self._parse_contracts(contracts, various_name, various_link)

            self._browser.close()
            self._browser.switch_to.window(self._page)

    def run(self):
        try:

            if not self._authorize:
                self._authorize_in_site()

            if self._authorize:
                self._load_contracts()

            print(f'Address = {self._address}. Parsing was finished ')

            print(f'Address = {self._address}. '
                  f'List of not pulled various links: {self._not_pulled_various_links}')

            print(f'Address = {self._address}. '
                  f'List of partially pulled various links: {self._partially_pulled_various_links}')

            print(f'Address = {self._address}. '
                  f'List of empty links: {self._not_parsed_links}')
            
            
            self._browser.quit()

        except KeyboardInterrupt:
            self._browser.quit()
            logging.error(f'Address = {self._address}. Parsing was not finished: KeyboardInterrupt')

        except Exception as exc:
            self._browser.quit()
            logging.error(f'Address = {self._address}. Parsing was not finished: {exc}')
