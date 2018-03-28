# coding=utf-8
from lib import Browser
from lib import Shopee
from selenium.common.exceptions import TimeoutException as TE
import configparser
import requests
import json
from urllib import parse
import pandas
from time import strftime
import time
from selenium.webdriver.common.keys import Keys
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium



def login(persist_cookie):
    today = strftime('%Y-%m-%d')
    cookie_file = 'cookies.pkl'
    config = configparser.ConfigParser()
    config.read('app.cnf')
    account = config['shopee']['account']
    password = config['shopee']['password']
    browser = Browser()
    try:
        browser.go(Shopee.login_page_url)
        browser.load_cookie_from(cookie_file)  
        browser.send_by_css(Shopee.account_input_css_selector, account)
        browser.send_by_css(Shopee.password_input_css_selector, password)
        browser.click_by_xpath(Shopee.login_button_xpath)
        try:
            browser.wait_for(lambda driver: driver.find_element_by_css_selector(Shopee.verify_code_input_css_selector))
            browser.send_by_css(Shopee.verify_code_input_css_selector, input('input verify code: '))
            browser.click_by_xpath(Shopee.verify_button_xpath)
        except TE:
            pass
        browser.wait_for(lambda driver: driver.current_url == Shopee.home)
        browser.click_by_xpath(Shopee.toship_button_xpath)

        browser.wait_for(lambda driver: driver.current_url == Shopee.home_export)
        '''
        time.sleep(3)
        for i in range(0,10):
            browser.send_by_xpath(Shopee.input_date_css_selector_xpath,Keys.BACK_SPACE)
            # time.sleep(1)
        browser.send_by_xpath(Shopee.input_date_css_selector_xpath,today)
        time.sleep(2)
        browser.click_by_xpath(Shopee.export_excel_xpath)
        
        # browser.wait_for(lambda driver: driver.current_url == Shopee.home_export)
        # cookie = browser.get_cookies()
        # cookie_string = ';'.join(['{}={}'.format(item.get('name'), item.get('value')) for item in cookie])
        # spc_cds = [item.get('value') for item in cookie if item.get('name') == 'SPC_CDS'][0]
        # path = '/api/v1/orders/259405162/?SPC_CDS=&SPC_CDS_VER=2'.format(spc_cds)
        # conn = requests.Session()
        # cat_header = Shopee.general_header.copy()
        # cat_header['method'] = 'GET'
        # cat_header['path'] = path
        # cat_header['cookie'] = cookie_string
        # conn.get(shopee.home+path, headers=cat_header)
        time.sleep(5)
        browser.click_by_xpath(Shopee.portal_sale_ship)
        browser.wait_for(lambda driver: driver.current_url == Shopee.home_toship8)
        browser.click_by_xpath(Shopee.checkbox_click_xpath)
        browser.send_by_css(Shopee.input_send_name_css_selector,"周凱旋")
        # browser.click_by_xpath(Shopee.button_sendnum_xpath)
        '''
        time.sleep(3)
        browser.go(Shopee.home_toship7)
        browser.wait_for(lambda driver: driver.current_url == Shopee.home_toship7)
        browser.click_by_xpath(Shopee.checkbox_click_xpath)
        # browser.click_by_xpath(Shopee.button_sendnum_xpath)
        time.sleep(3)
        browser.go(Shopee.home_toship25)
        browser.wait_for(lambda driver: driver.current_url == Shopee.home_toship25)
        browser.click_by_xpath(Shopee.checkbox_click_xpath)
        time.sleep(3)
        browser.send_by_css(Shopee.input_send_name_css_selector,"周凱旋")
        # browser.click_by_xpath(Shopee.button_sendnum_xpath)
        time.sleep(3)
        browser.click_by_xpath(Shopee.button_download_toship_xpath)
        browser.click_by_xpath(Shopee.checkbox_click_xpath_1)
        browser.click_by_xpath(Shopee.checkbox_click_send_xpath)
        #
        time.sleep(3)
        browser.go(Shopee.home_toship7_print)
        browser.click_by_xpath(Shopee.checkbox_click_xpath_1)
        browser.click_by_xpath(Shopee.checkbox_click_send_xpath)
        #
        time.sleep(3)
        browser.go(Shopee.home_toship8_print)
        browser.click_by_xpath(Shopee.checkbox_click_xpath_1)
        browser.click_by_xpath(Shopee.checkbox_click_send_xpath)
        # browser.click_by_xpath(Shopee.find_shipid_xpath)
        
        # browser.go()
        #
        # time.sleep(50000)


        # https://seller.shopee.tw/api/v1/orders/?limit=20&offset=0&shipping_method=%5B8%5D&type=toship&SPC_CDS=4ead7f7e-3a33-4a82-8b9a-430e4b0596e0&SPC_CDS_VER=2
        # https://seller.shopee.tw/api/v1/orders/259405162/?SPC_CDS=73f0bcc5-c377-4ce4-9318-8616ab8ddcd9&SPC_CDS_VER=2
        cookie = browser.get_cookies()
        cookie_string = ';'.join(['{}={}'.format(item.get('name'), item.get('value')) for item in cookie])
        spc_cds = [item.get('value') for item in cookie if item.get('name') == 'SPC_CDS'][0]
        # path = '/api/v1/orders/259405162/?SPC_CDS={}&SPC_CDS_VER=2'.format(spc_cds)
        path = '/api/v1/orders/?limit={0}&offset=0&shipping_method=%5B8%5D&type=toship&SPC_CDS={1}&SPC_CDS_VER=2'.format('40',spc_cds)
        conn = requests.Session()
        cat_header = Shopee.general_header.copy()
        cat_header['method'] = 'GET'
        cat_header['path'] = path
        cat_header['Content-Type'] = 'application/json;charset=utf-8'
        cat_header['cookie'] = cookie_string
        res = conn.get('https://seller.shopee.tw'+path, headers=cat_header)
        # print(res.text.replace('\\\\','\\'))
        # print(abc)
        # print()
        # print(res.content.decode("utf-8"))
        # #json_string = json.dumps(res.json(), ensure_ascii=False).replace('\\\\','\\')
        # save_json(res.json(), 'orders.json')
        for i in range(0,len(res.json()['orders'])):
            abc= res.json()['orders'][i]['id']
            print(abc)
            path1='https://seller.shopee.tw/portal/sale/'+str(abc)
            browser.go(path1)
            browser.wait_for(lambda driver: driver.current_url == path1)
            
            a=browser.find_text('/html/body/div/div/div[3]/div/div[1]/div[3]/div[1]/div/div[2]')
            b=browser.find_text('/html/body/div/div/div[3]/div/div[1]/div[3]/div[2]/div/div[2]')
            c=browser.find_text('/html/body/div/div/div[3]/div/div[1]/div[3]/div[3]/div/div[2]')

            print(a,b,c)
            time.sleep(3)
            

        time.sleep(8000)
            # cookie = browser.get_cookies()
            # cookie_string = ';'.join(['{}={}'.format(item.get('name'), item.get('value')) for item in cookie])
            # spc_cds = [item.get('value') for item in cookie if item.get('name') == 'SPC_CDS'][0]
            # path = '/api/v1/orders/{0}/?SPC_CDS={1}&SPC_CDS_VER=2'.format(res.json()['orders'][i]['id'],spc_cds)
            # conn = requests.Session()
            # cat_header = Shopee.general_header.copy()
            # cat_header['method'] = 'GET'
            # cat_header['path'] = path
            # cat_header['cookie'] = cookie_string
            # res = conn.get('https://seller.shopee.tw'+path, headers=cat_header)
            # save_json(res.json(), 'order0.json')
        if persist_cookie:
            browser.dump_cookie(cookie_file)
    except Exception as e:
        print(e)


    finally:
        browser.quit()


def save_json(data, save_to):
    with open(save_to, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


def main():
    login(True)
    # cookie_string = ';'.join(['{}={}'.format(item.get('name'), item.get('value')) for item in cookie])
    # spc_cds = [item.get('value') for item in cookie if item.get('name') == 'SPC_CDS'][0]
    # conn = requests.Session()
    # path = 'portal/sale?shipping_center_status=pickup_pending&type=toship'.format(spc_cds)

    # # get categories
    # conn = requests.Session()
    # path = '/api/v1/categories/?SPC_CDS={}&SPC_CDS_VER=2'.format(spc_cds)
    # cat_header = Shopee.general_header.copy()
    # cat_header['method'] = 'GET'
    # cat_header['path'] = path
    # cat_header['cookie'] = cookie_string
    # res = conn.get(Shopee.home + path, headers=cat_header)
    # save_json(res.json(), 'categories.json')
    # print(pandas.DataFrame(res.json()))
    # # get attributes
    # for cat in res.json()['categories']:
    #     try:
    #         cat_id = cat['id']
    #         catids_encoded = parse.quote('[{}]'.format(cat_id))
    #         path = '/api/v1/categories/attributes/?catids={}&SPC_CDS={}&SPC_CDS_VER=2'.format(catids_encoded, spc_cds)
    #         attr_header = Shopee.general_header.copy()
    #         attr_header['method'] = 'GET'
    #         attr_header['path'] = path
    #         attr_header['cookie'] = cookie_string
    #         res = conn.get(Shopee.home + path, headers=attr_header)
    #         save_json(res.json(), './json/attributes/' + str(cat_id) + '.json')

    #         # get items
    #         meta = res.json()['categories'][0]['meta']
    #         if 'modelid' in meta:
    #             model_id = str(meta['modelid'])
    #             path = '/api/v1/categories/attributes/?SPC_CDS={}&SPC_CDS_VER=2'.format(spc_cds)
    #             item_header = Shopee.general_header.copy()
    #             item_header['method'] = 'POST'
    #             item_header['path'] = path
    #             item_header['cookie'] = cookie_string
    #             item_header['content-length'] = '30'
    #             item_header['content-type'] = 'application/json'
    #             item_header['origin'] = 'https://seller.shopee.tw'
    #             res = conn.post(Shopee.home + path, headers=item_header,
    #                             json=json.loads('[{"values":[],"modelid":' + model_id + '}]'))
    #             save_json(res.json(), './json/items/' + model_id + '.json')

    #     except ValueError:
    #         print('Decoding JSON has failed \r\n {}'.format(res.text()))


if __name__ == '__main__':
    main()
