import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import os
import csv
import pymysql.cursors

config = {
    'host':'192.168.0.10',
    'port':3306,
    'user':'root',
    'password':'power&mis',
    'db':'classid',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
    }
# Connect to the database
connection = pymysql.connect(**config)

y=0
pathName = 'd:\\pcpong\\pic\\1\\'

while y == 0:
    x=input('請輸入 1 或 2 選擇要搜尋的網頁：\n1. 台北群加。\n2. 上海群加。\n3. 結束程式。\n-> ')

    if x == '1':
        url_1='http://www.powersync.com.tw/products_search.php'
        url_2='http://www.powersync.com.tw/'


        with open('d:\\pcpong\\python\\1.csv',encoding='utf-8') as csvfile1:

            readCSV = csv.reader(csvfile1,delimiter=',')

            x=[]
            for row in readCSV:
                z=[]
                print(row[0])
                z.append(str(row[0]))
                payload= {'searchValue':row[0]}
                r = requests.get(url_1,params=payload)
                soup = BeautifulSoup(r.text, 'html.parser')
                for i in soup.find_all('a'):
                    if "detail" in i.get('href'):
                        # z.append(url_2+i.get('href'))
                        print(url_2+i.get('href'))
                        try:
                            with connection.cursor() as cursor:
                                sql = "UPDATE powersync_link SET Link_1='%s' WHERE SNo='%s';" % (url_2+i.get('href'),str(row[0]))
                                cursor.execute(sql)
                                connection.commit()
                        except Exception as f:
                            print(f.args[0],f.args[1])
    elif x == '2':
        url_1='http://www.powersync.com.cn/products_search.php'
        url_2='http://www.powersync.com.cn/'
        with open('d:\\pcpong\\python\\1.csv',encoding='utf-8') as csvfile1:
            readCSV = csv.reader(csvfile1,delimiter=',')
            x=[]
            for row in readCSV:
                z=[]
                print(row[0])
                z.append(str(row[0]))
                payload= {'searchValue':row[0]}
                r = requests.get(url_1,params=payload)
                soup = BeautifulSoup(r.text, 'html.parser')
                for i in soup.find_all('a'):
                    if "detail" in i.get('href'):
                        # z.append(url_2+i.get('href'))
                        print(url_2+i.get('href'))
                        try:
                            with connection.cursor() as cursor:
                                sql = "UPDATE powersync_link SET Link_1='%s' WHERE SNo='%s';" % (url_2+i.get('href'),str(row[0]))
                                cursor.execute(sql)
                                connection.commit()
                        except Exception as f:
                            print(f.args[0],f.args[1])
    else:
        exit()
