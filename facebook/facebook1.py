import requests
import pandas as pd 
from dateutil.parser import parse

#使用你自己的toke

token = 'EAACEdEose0cBABLDyzmSZBstZCNoocfYFkVbcLOC3NPwTJVorioUeG2sZCCNVHl10ZACAKvXDwPo1yaKm70ImHErNz4Rno6RqQi8UWflsUrDKhzhuLZCR7TFhCTJVmVylZAHc3v6YX3ZCYVWevMKnj2jCbVGyMrlZABl70rB1gxZBYvlOlaQkhbl7ZBBoNSafMUr4ZD' 
fanpage_id = '342571109112167'

#抓取貼文時間、ID、內文、分享內容

res = requests.get('https://graph.facebook.com/v2.10/{}/posts?limit=100&access_token={}'.format(fanpage_id, token))

#建立空的list

posts = []
page = 1
while 'paging' in res.json():
    print('目前正在抓取第%d頁' % page)
    
    for post in res.json()['data']:
            
        #透過貼文ID來抓取讚數與分享數

        res2 = requests.get('https://graph.facebook.com/v2.10/{}?fields=likes.limit(0).summary(True), shares&access_token={}'.format(post['id'], token))
        
        if 'likes' in res2.json():
            likes = res2.json()['likes']['summary'].get('total_count')
        else:
            likes = 0
            
        if 'shares' in res2.json():
            shares = res2.json()['shares'].get('count')
        else:
            shares = 0
        
        posts.append([parse(post['created_time']), 
                      post['id'], 
                      post.get('message'), 
                      post.get('story'), 
                      likes, 
                      shares
                     ])
        
    if 'next' in res.json()['paging']:
        res = requests.get(res.json()['paging']['next'])
        page += 1
    else:
        break
        
print('抓取結束!')

#檔案輸出

df = pd.DataFrame(posts)
df.columns = ['貼文時間', '貼文ID', '貼文內容', '分享內容', '讚數', '分享數']
df.to_csv('大鼻觀點.csv', index=False)
