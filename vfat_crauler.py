"""This module contains Web Client for Data Aggregator"""
import os
import sys
import time
import csv
import re

from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from constants import PATH_TO_METAMASK_EXTENSION_CRX_FILE
from constants import TIMEOUT_FOR_CONTRACTS_PAGE_LOADING
from constants import TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING
from constants import PASSWORD_FOR_METAMASK

from constants import CONTRACT_NAME_PATTERN_1
from constants import CONTRACT_NAME_PATTERN_2
from constants import CONTRACT_APR_PATTERN_1
from constants import CONTRACT_APR_PATTERN_2
from constants import HEADERS



def extract_contract_values(contract):
    pattern = re.search(CONTRACT_NAME_PATTERN_1, contract)

    if pattern is not None:
        names = re.findall(r"\w+", pattern[0])

    else:
        pattern = re.search(CONTRACT_NAME_PATTERN_2, contract)
        if pattern is not None:
            name = pattern[0].replace('Price:', '')
            names = [name, ' ']
        else:
            return None, None

    contract_apr = re.search(CONTRACT_APR_PATTERN_1, contract)

    if contract_apr is None:
        contract_apr = re.search(CONTRACT_APR_PATTERN_2, contract)
    
    if contract_apr is not None:
        contract_apr_value = contract_apr[0].replace('Year ', '')
        contract_apr_value = contract_apr_value.replace('%', '')
    else:
        return None, None
    return names, contract_apr_value
    


class VfatCrauler():
    """A class to perform vfat site crauling"""
    def __init__(self, address, page_name):
        self._page_name = page_name
        self._options = Options()
        self._options.add_extension(os.path.join(ROOT_DIR, PATH_TO_METAMASK_EXTENSION_CRX_FILE))
        self._options.add_argument(
            f"user-data-dir=EXTENSION_CONFIG_{page_name}")  # file to save metamask extensions parameters

        self._address = address
        self._autorized = False

        self._browser = webdriver.Chrome(options=self._options) 
        self._page = self._browser.current_window_handle  

        self._make_csv_file_ready()


    def _make_csv_file_ready(self):
        with open(f'{self._page_name}.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


    def _autorize_in_site(self):
        try:
            popup_pages = self._browser.window_handles
            self._browser.switch_to.window(popup_pages[0]) 
            time.sleep(10)
            user_password = WebDriverWait(self._browser, 
                          TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='password']")))
        
            user_password.send_keys(PASSWORD_FOR_METAMASK)

            WebDriverWait(self._browser, 
                          TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING).until(EC.element_to_be_clickable((By.CLASS_NAME, 'MuiButton-label'))).click()

            self._browser.close()
            self._autorized = True

            print(f'Autorization was accessed in {self._address}')
                    
        except Exception as exc:
                    print(f'Cant access autorization in {self._address}, because {exc}. Please restart the script')

    def _catch_contracts_table(self, various_name):
        self._browser.maximize_window()

        try:
            WebDriverWait(self._browser, 
                      TIMEOUT_FOR_CONTRACTS_PAGE_LOADING).until(EC.text_to_be_present_in_element((By.ID, 'log'), 'Total Staked'))
            return self._browser.find_element_by_id('log')
     
        except TimeoutException:

            return self._browser.find_element_by_id('log')


    def _parse_contracts(self, contracts_table, various_name):
        border_pharse = "Finished reading smart contracts."
        if contracts_table is not None:
            contracts = contracts_table.text
        else:
            print('Did not catch any contracts, something wrong with internet or web site. Please restart script')
            return

        starting_index = contracts.find(border_pharse)
        contracts = contracts[starting_index + len(border_pharse):]

        contracts = contracts.split('\n\n')
        
        for contract in tqdm(contracts, desc='Extracting name and apr from contracts and saving to csv'):
            names, apr = extract_contract_values(contract)
            if not various_name: 
                contract
            row_to_write = [self._page_name, various_name, names[0], names[1], apr]
            with open(f'{self._page_name}.csv', 'a+') as file:
               writer = csv.writer(file)
               writer.writerow(row_to_write)


    def _load_contracts(self):
        try: 

            self._browser.switch_to.window(self._page)
            self._browser.get(self._address)
            self._browser.maximize_window()

            for contract_sourse in tqdm(WebDriverWait(self._browser, 
                                                  TIMEOUT_FOR_CONTRACTS_PAGE_LOADING).until(
                                                       EC.presence_of_all_elements_located((By.LINK_TEXT, 'Various'))), 
                                                  desc='Iterating various links'):

                various_link = contract_sourse.get_attribute('href')
                various_name = os.path.basename(os.path.normpath(contract_sourse.get_attribute('href')))
          
                self._browser.execute_script(f"window.open('{various_link}','_blank')")
                self._browser.switch_to.window(self._browser.window_handles[-1])
                contracts_table = self._catch_contracts_table(various_name)    
                self._parse_contracts(contracts_table, various_name)
            
                self._browser.close()
                self._browser.switch_to.window(self._page)

        except Exception as exc:
            print(f'Catched error while loading contracts: {exc}')


    def run(self):
        try:
            if not self._autorized:
                self._autorize_in_site()


            if self._autorized:
                self._load_contracts()

            print('Parsing was finished')
            self._browser.quit()

        except KeyboardInterrupt:
            self._browser.quit()
            print('Parsing wasnt finished, because of KeyboardInterrupt')

        except Exception as exc:
            self._browser.quit()
            print(f'Parsing wasnt finished, because of {exc}')



