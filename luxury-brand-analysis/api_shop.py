#가격측정
import os
import sys
import urllib.request
import datetime
import time
import json
import numpy as np
import pandas as pd

client_id = ""
client_secret = ""

#CODE 1

def getRequestUrl(url) :
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-ID", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    
    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e :
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
    
#CODE 2

def getNaverSearch(node, srcText, start, display) :
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText),start,display)
    
    url = base + node + parameters
    responseDecode = getRequestUrl(url)
    
    if (responseDecode == None) :
        return None
    else :
        return json.loads(responseDecode)
    
#CODE 3

def getPostData(post, jsonResult, cnt) :
    title = post['title']
    brand = post['brand']
    maker = post['maker']
    lprice = int(post['lprice'])
    category1 = post['category1']
    category2 = post['category2']
    category3 = post['category3']
    
    if lprice > 1000000 and lprice < 100000000 and category1 == '패션잡화' and category2 == '여성가방' and category3 == '토트백' :
        jsonResult.append({'cnt':cnt, 'title':title, 'brand':brand, 'maker':maker, 'lprice':lprice, 'category1':category1, 'category2':category2, 'category3':category3})
    return

#CODE 0

def main() :
    node = 'shop'
    srcText = input('검색어를 입력하세요 : ')
    cnt = 0
    jsonResult = []
    
    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    total = jsonResponse['total']
    
    while ((jsonResponse != None) and (jsonResponse['display'] != 0)) :
        for post in jsonResponse['items'] :
            cnt += 1
            getPostData(post, jsonResult, cnt)
            
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)
        
    print('전체 검색 : %d 건' %total)
    
    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf-8') as outfile :
        jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii = False)
        
        outfile.write(jsonFile)
        
    print("가져온 데이터 : %d 건" %(cnt))
    print('%s_naver_%s.json SAVED' % (srcText, node))

if __name__ == '__main__' :
    main()
    
