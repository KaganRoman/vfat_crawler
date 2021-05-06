import os
import sys
import logging
import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# Must ne at the same folder with parse_site.py
PATH_TO_METAMASK_EXTENSION_CRX_FILE = 'extension_9_4_0_0.crx' 
TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING = 60
REDUCED_TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING = 9

# Password for metamask, doesnt need to be changed
PASSWORD_FOR_METAMASK = 'hellokitty'


class Browser:
    def __init__(self, network_name):
        self._network_name = network_name
        
    def __enter__(self):
        options = Options()
        options.add_extension(os.path.join(ROOT_DIR, PATH_TO_METAMASK_EXTENSION_CRX_FILE))
        options.add_argument(
            f"user-data-dir=browsers/EXTENSION_CONFIG_{self._network_name}")  # file to save metamask extensions parameters

        self._browser = webdriver.Chrome(options=options)
        self._page = self._browser.current_window_handle
        self._authorized_metamask = False
    
    def __exit__(self, type, value, traceback):
        self._browser.quit()

    def _authorize_metamask(self):
        if self._authorized_metamask:
            return
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
            self._authorized_metamask = True
            logging.info(f'Network = {self._network_name}. Metamask authorization was accessed')
        except Exception as exc:
            logging.error(f'Network = {self._network_name}. '
                          f'Please restart the script. Cant authorize in Metamask: {exc}')
            raise
    
    
    def load_page(self, url, retries, timeout, wait_condition):
        self._authorize_metamask()

        self._browser.switch_to.window(self._page)
        self._browser.get(url)

        for i in range(retries):
            try:
                return WebDriverWait(self._browser, timeout).until(wait_condition)
            except:
                self._browser.refresh()
                logging.error(
                    f'Address = {url}. Page is unavailable. Trying to reconnect.')

        logging.error(f'Address = {self._address}. Please restart script. '
                        f'Did not catch any various links, page is unavailable')        


    def find_element_by_id(self, id):
        return self._browser.find_element_by_id(id)