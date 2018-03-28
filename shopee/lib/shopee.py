class Shopee:
    home = 'https://seller.shopee.tw/'
    home_export = 'https://seller.shopee.tw/portal/sale?type=toship'
    home_toship8 = 'https://seller.shopee.tw/portal/sale/ship?categoryId=8'
    home_toship7 = 'https://seller.shopee.tw/portal/sale/ship?categoryId=7'
    home_toship25 = 'https://seller.shopee.tw/portal/sale/ship?categoryId=25'
    home_toship0 = 'https://seller.shopee.tw/portal/sale/ship?categoryId=0'
    home_toship8_print = 'https://seller.shopee.tw/portal/sale/ship?categoryId=8&type=print'
    home_toship7_print = 'https://seller.shopee.tw/portal/sale/ship?categoryId=7&type=print'
    home_toship25_print = 'https://seller.shopee.tw/portal/sale/ship?categoryId=25&type=print'

    login_page_url = 'https://seller.shopee.tw/account/signin'

    account_input_css_selector = "input[placeholder='email/ 手機號碼/ 使用者名稱']"

    password_input_css_selector = "input[placeholder='密碼']"

    login_button_xpath = "//div[contains(., '登入')][contains(@class, 'shopee-button')]"

    verify_code_input_css_selector = "input[placeholder='驗證碼']"

    verify_code_input_css_selector = "input[placeholder='驗證碼']"

    verify_button_xpath = "//div[contains(., '進行驗證')][contains(@class, 'shopee-button')]"

    toship_button_xpath = "//div[contains(., '我的銷售')][contains(@class, 'home-big-button__title')]"

    input_date_css_selector_xpath = "//div[contains(@class, 'input shopee-datepicker__input')]/child::input"

    portal_sale_ship = "//div[contains(., '出貨')][contains(@class, 'shopee-button__text')]"

    export_excel_xpath = "//div[contains(., '匯出')][contains(@class, 'shopee-button')]"

    input_send_name_css_selector = "input[placeholder='你的真實姓名']"

    checkbox_click_xpath = "//div[contains(@class, 'shopee-checkbox')][1]"
    checkbox_click_xpath_1 = "//div[contains(@class, 'mass-ship-list-item__selection--width')]"
    checkbox_click_send_xpath = "//div[contains(., '寄件單')][contains(@class, 'sc-label')]"

    button_sendnum_xpath = "//div[contains(., '產生寄件編號')][contains(@class, 'shopee-button__title')]"

    button_download_toship_xpath = "//a[contains(@class, 'tabs__tab')][contains(., '下載寄件單')]"

    find_shipid_xpath = "//a[contains(@class, 'ember-view')]"
    
    general_header = {  'authority':'seller.shopee.tw',
                        'scheme':'https',
                        'accept':'application/json, text/javascript, */*; q=0.01',
                        'accept-encoding':'gzip, deflate, br',
                        'accept-language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
                        'dnt': ';',
                        'referer':'https://seller.shopee.tw/portal/sale',
                        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}