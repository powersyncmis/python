import sys
import os
from pathlib import Path
import json
import pickle
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui

class Browser:
    def __init__(self):
        chrome_options = Options()
        prefs = {'download.default_directory':'C:\\temp'}   
        chrome_options.add_experimental_option('prefs', prefs)     
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(os.path.abspath('chromedriver.exe'), desired_capabilities = chrome_options.to_capabilities(),chrome_options=chrome_options)

        self.wait = ui.WebDriverWait(self.driver,8)

    def go(self, url):
        self.driver.get(url)
    
    def load_cookie_from(self, cookie_file):
        if(Path(cookie_file).exists()):
            for cookie in pickle.load(open(cookie_file, "rb")):
                #TODO it's a workaround
                if 'SPC_CDS' in json.dumps(cookie):
                    continue
                self.driver.add_cookie(cookie)
            #print('cookie loaded')

    def wait_for(self, method):
        self.wait.until(method)

    def find_by_css(self, path):
        self.wait_for(lambda driver: driver.find_element_by_css_selector(path))
        return self.driver.find_element_by_css_selector(path)

    def find_by_xpath(self, path):
        self.wait_for(lambda driver: driver.find_element_by_xpath(path))
        return self.driver.find_element_by_xpath(path)

    def finds_by_xpath(self, path):
        self.wait_for(lambda driver: driver.find_elements_by_xpath(path))
        return self.driver.find_elements_by_xpath(path)

    def find_text(self,path):
        self.wait_for(lambda driver: driver.find_element_by_xpath(path))
        return self.driver.find_element_by_xpath(path).text.replace("\\\\",'\\').encode('utf-8')

    def clean_by_xpath(self, path):
        input1 = self.driver.find_element_by_xpath(path)
        input1.clear

    def send_by_css(self, path, *keys):
        el = self.find_by_css(path)
        el.send_keys(*keys)

    def send_by_xpath(self, path, *keys):
        el = self.find_by_xpath(path)
        
        el.send_keys(*keys)

    def click_by_css(self, path):
        el = self.find_by_css(path)
        el.click()

    def click_by_xpath(self, path):
        el = self.find_by_xpath(path)
        el.click()
    
    def get_cookies(self):
        return self.driver.get_cookies()

    def dump_cookie(self, cookie_file):
        pickle.dump( self.driver.get_cookies() , open(cookie_file,"wb"))
        
    def quit(self):
        self.driver.quit()