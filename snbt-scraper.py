import time
from twikit import Client, Tweet
from typing import NoReturn
client = Client()
import json
idl=[]
i=0
INTERVAL = 60 * 5
SHORT_INTERVAL = 60*2
counter=0
USERNAME = ''
EMAIL = ''
PASSWORD = ''
DIR=''
def scraper_snbt():

    client = Client('en-US')

    client.login(
        auth_info_1=EMAIL ,
        password=PASSWORD
    )
    tweets = client.search_tweet('snbt day 1', 'Latest',)
    for tweet in tweets:
        lm2=""
        lm=tweet.media
        if type(lm) is list:
            lm2=lm[0]['display_url']
        tl=f"{tweet.user.name}:{tweet.text} | {lm2} | {tweet.created_at,} | {tweet.id}\n"
        if tl in idl:
            pass
        else:
            print(tl)
            idl.append(tl)
    counter+=1
    i+=1
    while i>0:
        next_tweet=tweets.next()
        for tweet in next_tweet:
            lm2=""
            lm=tweet.media
            if type(lm) is list:
                lm2=lm[0]['display_url']
            tl=f"{tweet.user.name}:{tweet.text} | {lm2} | {tweet.created_at,} | {tweet.id}\n"
            if tl in idl:
                pass
            else:
                print(tl)
                idl.append(tl)
        if tl == idl[-1]:
            time.sleep(INTERVAL)   
        else: 
            counter+=1
    time.sleep(INTERVAL)
    scraper_snbt()


def testl():
    ltest=[{'display_url': 'pic.twitter.com/pUaXGZPR4D', 'expanded_url': 'https://twitter.com/iloveyy0u/status/1784580874312536284/photo/1', 'id_str': '1784580865743532032', 'indices': [281, 304], 'media_key': '3_1784580865743532032', 'media_url_https': 'https://pbs.twimg.com/media/GMQa15-aMAAWliH.jpg', 'type': 'photo', 'url': 'https://t.co/pUaXGZPR4D', 'ext_media_availability': {'status': 'Available'}, 'features': {'large': {'faces': [{'x': 124, 'y': 262, 'h': 212, 'w': 212}]}, 'medium': {'faces': [{'x': 98, 'y': 209, 'h': 169, 'w': 169}]}, 'small': {'faces': [{'x': 56, 'y': 118, 'h': 95, 'w': 95}]}, 'orig': {'faces': [{'x': 124, 'y': 262, 'h': 212, 'w': 212}]}}, 'sizes': {'large': {'h': 1504, 'w': 1170, 'resize': 'fit'}, 'medium': {'h': 1200, 'w': 934, 'resize': 'fit'}, 'small': {'h': 680, 'w': 529, 'resize': 'fit'}, 'thumb': {'h': 150, 'w': 150, 'resize': 'crop'}}, 'original_info': {'height': 1504, 'width': 1170, 'focus_rects': [{'x': 0, 'y': 11, 'w': 1170, 'h': 655}, {'x': 0, 'y': 0, 'w': 1170, 'h': 1170}, {'x': 0, 'y': 0, 'w': 1170, 'h': 1334}, {'x': 187, 'y': 0, 'w': 752, 'h': 1504}, {'x': 0, 'y': 0, 'w': 1170, 'h': 1504}]}, 'allow_download_status': {'allow_download': True}, 'media_results': {'result': {'media_key': '3_1784580865743532032'}}}, {'display_url': 'pic.twitter.com/pUaXGZPR4D', 'expanded_url': 'https://twitter.com/iloveyy0u/status/1784580874312536284/photo/1', 'id_str': '1784580865731022849', 'indices': [281, 304], 'media_key': '3_1784580865731022849', 'media_url_https': 'https://pbs.twimg.com/media/GMQa157bUAE3nw_.jpg', 'type': 'photo', 'url': 'https://t.co/pUaXGZPR4D', 'ext_media_availability': {'status': 'Available'}, 'features': {'large': {'faces': []}, 'medium': {'faces': []}, 'small': {'faces': []}, 'orig': {'faces': []}}, 'sizes': {'large': {'h': 1979, 'w': 1979, 'resize': 'fit'}, 'medium': {'h': 1200, 'w': 1200, 'resize': 'fit'}, 'small': {'h': 680, 'w': 680, 'resize': 'fit'}, 'thumb': {'h': 150, 'w': 150, 'resize': 'crop'}}, 'original_info': {'height': 1979, 'width': 1979, 'focus_rects': [{'x': 0, 'y': 781, 'w': 1979, 'h': 1108}, {'x': 0, 'y': 0, 'w': 1979, 'h': 1979}, {'x': 243, 'y': 0, 'w': 1736, 'h': 1979}, {'x': 642, 'y': 0, 'w': 990, 'h': 1979}, {'x': 0, 'y': 0, 'w': 1979, 'h': 1979}]}, 'media_results': {'result': {'media_key': '3_1784580865731022849'}}}]
    ltjson=json.dumps(ltest)
    print(f"https://{ltest[0]['display_url']}")

def nexttwtdebug(num:int, t:int):
    while num>0:
        t+=1
        num-=1
    return t

def snbt_scraper_simple(counter:int,search:str):
    f=open(DIR,"a")
    client = Client('en-US')
    client.login(
        auth_info_1=USERNAME,
        auth_info_2= EMAIL,
        password=PASSWORD
    )
    tweets = client.search_tweet(search, 'Latest',)
    for tweet in tweets:
        lm2="no media"
        lm=tweet.media
        if type(lm) is list:
            lm2=f"https://{lm[0]['display_url']}"
        tl=f"{tweet.user.name} | {tweet.text} | {lm2} | {tweet.created_at,} | {tweet.id} | https://twitter.com/{tweet.user.screen_name}/status/{tweet.id} \n"
        f.write(tl)
        if tl in idl:
            pass
        else:
            print(tl)
            idl.append(tl)
    counter+=1
    while counter>0:
        next_tweet=tweets.next()
        counter-=1
    for tweet in next_tweet:
        lm2="no media"
        lm=tweet.media
        if type(lm) is list:
            lm2=f"https://{lm[0]['display_url']}"
        tl=f"{tweet.user.name} | {tweet.text} | {lm2} | {tweet.created_at,} | {tweet.id} | https://twitter.com/{tweet.user.screen_name}/status/{tweet.id} \n"
        f.write(tl)
        if tl in idl:
            pass
        else:
            print(tl)
            idl.append(tl)
        if tl == idl[0]:
            print("went to the beginning again sleeping") 
            time.sleep(INTERVAL)   
    print("sleeping to prevent rate limit")
    time.sleep(SHORT_INTERVAL)
    if tl != idl[0]:
        counter+=1
        if counter>5:
            print("emergency trigger sleeping")
            time.sleep(INTERVAL)
        else:
            snbt_scraper_simple(0,'snbt')
    else:
        print("went to the beginning again sleeping") 
        time.sleep(INTERVAL)
    
    if counter>5:
        print("emergency breakout to prevent rate limit sleeping")
        time.sleep(INTERVAL)
    
    print("emergency breakout to prevent rate limit sleeping")
    time.sleep(INTERVAL)
    
def testscrape(counter:int,search:str):
    client = Client('en-US')

    client.login(
        auth_info_1=USERNAME,
        auth_info_2= EMAIL,
        password=PASSWORD
    )
    tweets = client.search_tweet(search, 'Latest',count=1)
    for tweet in tweets:
        lm2="no media"
        lm=tweet.media
        if type(lm) is list:
            lm2=lm[0]['display_url']
        tl=f"{tweet.user.name} | {tweet.text} | {lm2} | {tweet.created_at,} | {tweet.id} | https://twitter.com/{tweet.user.screen_name}/status/{tweet.id} \n"
    return tl
    
#snbt_scraper_simple(0,'snbt day 1')
testl()

#scraper_snbt()

