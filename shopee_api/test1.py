import datetime
import hashlib
import hmac
import json
import time

import requests
import xlwt

import pyodbc

# 建立excel檔紀錄訂單
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'shope', cell_overwrite_ok=True)
row0 = [u'日期', u'訂單編號', u'訂單狀態', u'姓名', u'電話', u'地址', u'包裹號碼',
        u'訂單金額', u'實付總金額', u'品號', u'單價', u'數量', u'單別', u'單號', u'客戶代碼']
for q in range(0, len(row0)):
    sheet1.write(0, q, row0[q])

# 連接鼎新ERP
server = '192.168.0.5'
database = 'Leader'
username = 'sa'
password = 'dsc@54302158'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()


'''
url = "https://partner.shopeemobile.com/api/v1/orders/detail"
payload = '{"ordersn_list":["18010516049JGAB"],"partner_id":70076,"shopid":10966219,"timestamp":' + str(timestamp) +"}"
secret_key = b"ed2b432a45c45a74eb995670b58f4f09d62655095da907326a7a0b7fbe6fccee"
len1=len(payload)
message = url + "|" + payload
hash_sha = hmac.new(secret_key,message.encode('utf-8'),hashlib.sha256).hexdigest()
headers = {'Content-Type': 'application/json', 'Authorization': hash_sha, 'content-length': str(len1)}
response = requests.request("POST", url, data=payload, headers=headers)
data = json.loads(response.text)
print(data)
'''

y = 0
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
filename = datetime.datetime.fromtimestamp(ts).strftime('%g%m%d_%H%M%S')
# 取得今天日期 格式： 2018-01-01
timestamp = int(time.time())
a = st + " 00:00:00"
b = st + " 23:59:59"
timeA = time.strptime(a, "%Y-%m-%d %H:%M:%S")
timeB = time.strptime(b, "%Y-%m-%d %H:%M:%S")
t1 = int(time.mktime(timeA))
t2 = int(time.mktime(timeB))

url = "https://partner.shopeemobile.com/api/v1/orders/basics"
payload = '{"create_time_from":' + str(t1) + ',"create_time_to":' + str(
    t2) + ',"pagination_entries_per_page":100,"pagination_offset":0,"partner_id":70076,"shopid":10966219,"timestamp":' + str(timestamp) + "}"
secret_key = b"ed2b432a45c45a74eb995670b58f4f09d62655095da907326a7a0b7fbe6fccee"
len1 = len(payload)
message = url + "|" + payload
hash_sha = hmac.new(secret_key, message.encode(
    'utf-8'), hashlib.sha256).hexdigest()
headers = {'Content-Type': 'application/json',
           'Authorization': hash_sha, 'content-length': str(len1)}
response = requests.request("POST", url, data=payload, headers=headers)
data = json.loads(response.text)
# print(data['orders'])
w = 0
u = 0
for i in data['orders']:
    x = i['ordersn']
    timestamp = int(time.time())
    url = "https://partner.shopeemobile.com/api/v1/orders/detail"
    payload = '{"ordersn_list":["' + x + \
        '"],"partner_id":70076,"shopid":10966219,"timestamp":' + \
        str(timestamp) + "}"
    secret_key = b"ed2b432a45c45a74eb995670b58f4f09d62655095da907326a7a0b7fbe6fccee"
    len2 = len(payload)
    message = url + "|" + payload
    hash_sha = hmac.new(secret_key, message.encode(
        'utf-8'), hashlib.sha256).hexdigest()
    headers = {'Content-Type': 'application/json',
               'Authorization': hash_sha, 'content-length': str(len2)}
    response = requests.request("POST", url, data=payload, headers=headers)
    data2 = response.text
    # print(data)
    y = len(data2)
    z = 0
    q = 0

    # if str(data)[str(data).find('order_status', 0, len(data)) + 15:str(data).find('"', str(data).find('order_status', 0, len(data)) + 15)] != "READY_TO_SHIP" and str(data)[str(data).find('order_status', 0, len(data)) + 15:str(data).find('"', str(data).find('order_status', 0, len(data)) + 15)] != "SHIPPED":
    #     continue
    w = w + 1
    u = u + 1
    x1 = str(data2)[str(data2).find('order_status', 0, y) + 15:str(
        data2).find('"', str(data2).find('order_status', 0, y) + 15)]
    x2 = str(data2)[str(data2).find('name', 0, y) +
                    7:str(data2).find('"', str(data2).find('name', 0, y) + 7)]
    x3 = str(data2)[str(data2).find('phone', 0, y) +
                    8:str(data2).find('"', str(data2).find('phone', 0, y) + 8)]
    x4 = str(data2)[str(data2).find('full_address', 0, y) + 15:str(
        data2).find('"', str(data2).find('full_address', 0, y) + 15)]
    x5 = str(data2)[str(data2).find('tracking_no', 0, y) + 14:str(
        data2).find('"', str(data2).find('tracking_no', 0, y) + 14)]
    x6 = str(data2)[str(data2).find('escrow_amount', 0, y) + 16:str(
        data2).find('"', str(data2).find('escrow_amount', 0, y) + 16)]
    x7 = str(data2)[str(data2).find('total_amount', 0, y) + 15:str(
        data2).find('"', str(data2).find('total_amount', 0, y) + 15)]
    # print("\n\n訂單編號：" + x)
    # print("訂單狀態：" + x1)
    # print("姓    名：" + x2)
    # print("電    話：" + x3)
    # print("地    址：" + x4)
    # print("包裹號碼：" + x5)
    # print("訂單金額：" + x6)
    # print("實付金額：" + x7 + "\n-------------------------------------------------------")
    sheet1.write(u, 0, st)
    sheet1.write(u, 1, x)
    sheet1.write(u, 2, x1)
    sheet1.write(u, 3, x2)
    sheet1.write(u, 4, x3)
    sheet1.write(u, 5, x4)
    sheet1.write(u, 6, x5)
    sheet1.write(u, 7, x6)
    sheet1.write(u, 8, x7)

    var1 = '%%' + x + '%%'
    cursor.execute(
        "SELECT TC001,TC002,TC004 FROM COPTC WHERE TC012 LIKE '%s'" % (var1))
    row = cursor.fetchone()
    if row is not None:
        sheet1.write(u, 12, str(row[0]))
        sheet1.write(u, 13, str(row[1]))
        sheet1.write(u, 14, str(row[2]))

    while 1:
        q = str(data2).find('item_sku', z, y)
        q_start = q + 11
        if q == -1:
            break
        q_end = str(data2).find(',', q, y)
        item1 = str(data2)[q_start:q_end - 1].strip()
        z = q_end

        q = str(data2).find('variation_discounted_price', z, y)
        q_start = q + 29
        if q == -1:
            break
        q_end = str(data2).find(',', q, y)
        price = str(data2)[q_start:q_end - 1].strip()
        z = q_end

        q = str(data2).find('variation_quantity_purchased', z, y)
        q_start = q + 31
        q_end = str(data2).find(',', q, y)
        value = str(data2)[q_start-1:q_end].strip()
        z = q_end

        q = str(data2).find('variation_sku', z, y)
        q_start = q + 16
        q_end = str(data2).find(',', q, y)
        item = str(data2)[q_start:q_end - 1].strip()
        z = q_end + 1

        if item == '':
            item = item1
        else:
            item = item
        # print("    品號：{0:18s} 金額：{1:5s} 數量：{2:2s}".format(item, str(price), str(value)))
        sheet1.write(u, 9, item)
        sheet1.write(u, 10, str(price))
        sheet1.write(u, 11, str(value))
        u = u + 1

sheet1.col(0).width = 3000
sheet1.col(1).width = 5000
sheet1.col(2).width = 4500
sheet1.col(3).width = 2000
sheet1.col(4).width = 3500
sheet1.col(5).width = 20000
sheet1.col(6).width = 4000
sheet1.col(7).width = 1500
sheet1.col(8).width = 1500
sheet1.col(9).width = 5500
sheet1.col(10).width = 1500
sheet1.col(11).width = 1500
sheet1.col(12).width = 1500
sheet1.col(13).width = 3000
sheet1.col(14).width = 2000

f.save(filename + '.xls')
print("\n總計：{0:4s} 筆訂單".format(str(w)))


# for j in data['orders']:
#     x = j['ordersn']
#     timestamp = int(time.time())
#     url = "https://partner.shopeemobile.com/api/v1/logistics/init_parameter/get"
#     payload = '{"ordersn":"' + x + \
#         '","partner_id":70076,"shopid":10966219,"timestamp":' + \
#         str(timestamp) + "}"
#     secret_key = b"ed2b432a45c45a74eb995670b58f4f09d62655095da907326a7a0b7fbe6fccee"
#     len3 = len(payload)
#     message = url + "|" + payload
#     hash_sha = hmac.new(secret_key, message.encode(
#         'utf-8'), hashlib.sha256).hexdigest()
#     headers = {'Content-Type': 'application/json',
#                'Authorization': hash_sha, 'content-length': str(len3)}
#     response = requests.request("POST", url, data=payload, headers=headers)
#     data3 = response.text
#     print(data3)
#     y = len(data3)
