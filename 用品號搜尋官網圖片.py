import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import os
import csv

y=0
pathName = 'd:\\pcpong\\pic\\1\\'

while y == 0:
    x=input('請輸入 1 或 2 選擇要搜尋的網頁：\n1. 台北群加。\n2. 上海群加。\n3. 結束程式\n-> ')

    if x == '1':
        url_1='http://www.powersync.com.tw/products_search.php'
        url_2='http://www.powersync.com.tw/'
        y=1
        with open('d:\\pcpong\\python\\1.csv',encoding='utf-8') as csvfile:
            readCSV = csv.reader(csvfile,delimiter=',')
            for row in readCSV:
                print(row[0])
                payload= {'searchValue':row[0]}
                r = requests.get(url_1,params=payload)
                soup = BeautifulSoup(r.text, 'html.parser')
                zzz=0
                for i in  soup.select('img'):
                    if "up" in i.get('src') and zzz==0:

                        z=url_2+i.get('src')
                        print(z)
                        response = urllib.request.urlopen(z)
                        img_bytes = response.read()
                        f=open(pathName+row[0]+'.png',"wb")
                        f.write(img_bytes)
                        f.close()
                        zzz=zzz+1
                    elif "up" in i.get('src') and zzz>0:
                        z=url_2+i.get('src')
                        response = urllib.request.urlopen(z)
                        img_bytes = response.read()
                        f=open(pathName+row[0]+'.jpg',"wb")
                        f.write(img_bytes)
                        f.close()
                        zzz=zzz+1
    elif x == '2':
        url_1='http://www.powersync.com.cn/products_search.php'
        url_2='http://www.powersync.com.cn/'
        y=1
        with open('d:\\pcpong\\python\\1.csv',encoding='utf-8') as csvfile:
            readCSV = csv.reader(csvfile,delimiter=',')
            for row in readCSV:
                print(row[0])
                payload= {'searchValue':row[0]}
                r = requests.get(url_1,params=payload)
                soup = BeautifulSoup(r.text, 'html.parser')
                zzz=0
                for i in  soup.select('img'):
                    if "up" in i.get('src') and zzz==0:

                        z=url_2+i.get('src')
                        print(z)
                        response = urllib.request.urlopen(z)
                        img_bytes = response.read()
                        f=open(pathName+row[0]+'.png',"wb")
                        f.write(img_bytes)
                        f.close()
                        zzz=zzz+1
                    elif "up" in i.get('src') and zzz>0:
                        z=url_2+i.get('src')
                        response = urllib.request.urlopen(z)
                        img_bytes = response.read()
                        f=open(pathName+row[0]+'.jpg',"wb")
                        f.write(img_bytes)
                        f.close()
                        zzz=zzz+1
    else:
        exit()


