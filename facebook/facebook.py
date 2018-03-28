import requests
import pandas as pd 
from dateutil.parser import parse


#在Facebook Graph API Exploer取得token以及粉絲專頁的ID


token = 'EAACEdEose0cBABLDyzmSZBstZCNoocfYFkVbcLOC3NPwTJVorioUeG2sZCCNVHl10ZACAKvXDwPo1yaKm70ImHErNz4Rno6RqQi8UWflsUrDKhzhuLZCR7TFhCTJVmVylZAHc3v6YX3ZCYVWevMKnj2jCbVGyMrlZABl70rB1gxZBYvlOlaQkhbl7ZBBoNSafMUr4ZD' 
fanpage_id = '342571109112167'

#建立一個空的list          


information_list = []


#目標頁面


res = requests.get('https://graph.facebook.com/v2.10/{}/posts?limit=100&access_token={}'.format(fanpage_id, token))
page = 1  


#API最多一次呼叫100筆資料，因此使用while迴圈去翻頁取得所有的文章


while 'paging' in res.json(): 
    for index, information in enumerate(res.json()['data']):
        print('正在爬取第{}頁，第{}篇文章'.format(page, index + 1))
        
        
        #判斷是否為發文，是則開始蒐集按讚ID


        if 'message' in information:
            res_post = requests.get('https://graph.facebook.com/v2.10/{}/likes?limit=1000&access_token={}'.format(information['id'], token))
            
            
            #判斷按讚人數是否超過1000人，若超過則需要翻頁擷取；當沒有人按讚時，按讚人名與ID皆為NO

            try:
                if 'next' not in res_post.json()['paging']:
                    for likes in res_post.json()['data']:
                        information_list.append([information['id'], information['message'], parse(information['created_time']).date(), likes['id'], likes['name']])                
                elif 'next' in res_post.json()['paging']:
                    while 'paging' in res_post.json():
                        for likes in res_post.json()['data']:
                            information_list.append([information['id'], information['message'], parse(information['created_time']).date(), likes['id'], likes['name']])
                        if 'next' in res_post.json()['paging']:
                            res_post = requests.get(res_post.json()['paging']['next'])
                        else:
                            break
                for i in information_list:
                    print(i[1])
            except:
                information_list.append([information['id'], information['message'], parse(information['created_time']).date(), "NO", "NO"])

    if 'next' in res.json()['paging']:                
        res = requests.get(res.json()['paging']['next'])
        page += 1
    else:
        break
        
print('爬取結束!')
