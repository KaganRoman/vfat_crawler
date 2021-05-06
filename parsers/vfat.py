import time
import os
import logging
from tqdm import tqdm

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from parsers.vfat_parser import parse_contracts, TOTAL_STAKED
from config import Blockchain


VFAT_LINKS = {
    Blockchain.ETH: 'https://vfat.tools',
    Blockchain.BSC: 'https://vfat.tools/bsc',
    Blockchain.HECO: 'https://vfat.tools/heco',
}

EXCLUDE_LIST = {
    Blockchain.ETH: ['https://vfat.tools/aave/'],
    Blockchain.BSC: ['https://vfat.tools/bsc/beefy/'],
    Blockchain.HECO: [] 
}

LINKS_WAIT_CONDITION = EC.presence_of_all_elements_located(
    (By.LINK_TEXT, 'Various'))

PAGE_WAIT_CONDITION = EC.text_to_be_present_in_element(
    (By.ID, 'log'), TOTAL_STAKED)

TIMEOUT_FOR_CONTRACTS_PAGE_LOADING = 60
TIMEOUT_FOR_VERBOSE_PAGE_LOADING = 60

POST_LOADING_SLEEP = 5
NUMBER_OF_REFRESH_TRIES = 3


class Vfat:
    def __init__(self, blockchain):
        self._blockchain = blockchain
        self._failed_links = []

    def extract(self, browser, include_list):
        links = self._get_links(browser, include_list)
        return self._parse_links(browser, links)

    def _get_links(self, browser, include_list):
        if include_list:
            return include_list
        links_content = browser.load_page(VFAT_LINKS[self._blockchain],
                                          NUMBER_OF_REFRESH_TRIES,
                                          TIMEOUT_FOR_CONTRACTS_PAGE_LOADING,
                                          LINKS_WAIT_CONDITION)
        links = self._parse_links_content(links_content)
        return [l for l in links if l not in EXCLUDE_LIST]

    def _parse_links(self, browser, links):
        results = []
        for link in tqdm(links, desc="vfat links"):
            rows = self._parse_link(browser, link)
            if rows:
                results.extend(rows)
            else:
                self._failed_links.append(l)
        print(f'Tried to parse {len(links)} links, found {len(results)} rows, failed to parse: {self._failed_links}')
        return results
                
    def _parse_link(self, browser, link):
        try:
            print(f'Loading {link}')
            browser.load_page(link, NUMBER_OF_REFRESH_TRIES,
                            TIMEOUT_FOR_VERBOSE_PAGE_LOADING, PAGE_WAIT_CONDITION)
            time.sleep(POST_LOADING_SLEEP)
            content = browser.find_element_by_id('log').text
            return self._parse_contracts(content, link)
        except Exception as exc:
            logging.error(f'Failed to parse {link}. {exc}')
        return None

    def _parse_links_content(self, content):
        return [v.get_attribute('href') for v in content]

    def _parse_contracts(self, content, link):
        protocol = os.path.basename(os.path.normpath(link))
        return parse_contracts(content, self._blockchain, protocol, link)
