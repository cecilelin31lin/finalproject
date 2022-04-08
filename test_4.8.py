# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:44:47 2022

@author: w2000
"""

import urllib.request as req
#pip install beautifulsoup4
#from bs4 import BeautifulSoup 都失敗ㄟ
import bs4
import os, time
import jieba.posseg as psg


def NOOB_crawling(url):
    request=req.Request(url, headers={"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}) #f12 headers是正常使用者在訪問網頁時會留下的資料，寫近來ip才不會被封鎖
    with req.urlopen(url) as response:
        data=response.read().decode(encoding="utf-8") #harry potter text gbk、ISO...、uft8無法解碼，怎麼辦?
    root=bs4.BeautifulSoup(data,"lxml") #lxml是在解析甚麼，印出來看起來跟utf8解出來一樣
    txts=root.find("pre", id="SourceText")
    return txts

with open(file="harry_potter_s1", mode="w", encoding="utf8") as file:
    for i in range(1,18):
        url="http://www.haodoo.net/?M=u&P=G1278:%d&L=book" %(i)
        dict={}
        for txt in NOOB_crawling(url): #時間複雜度會比 txts=NOOB_crawling for txt in txts高嗎?
            file.write(txt)
            words=psg.cut(txt)
            for word in words:
                if word.flag=="nr" and word.word in dict:
                    dict[word.word]+=1
                elif word.flag =="nr" and word.word not in dict:
                    dict[word.word]=1
    time.sleep(3)
print(dict)

#小結: jieba有失敗的斷詞，無法正確斷出人名


'''
dict={}
with open(file="harry_potter_s1", mode="r", encoding="utf8") as file: #不是decoding喔!
#Python3的str 默認不是bytes，所以不能decode，只能先encode轉為bytes，再decode
#'builtin_function_or_method' object has no attribute 'decode' ????
    
    txt=file.readlines #讀取每行，到底需不需要，因為文本中有的沒有分行
    words=psg.cut(txt) #cut_all=False 精確分析模式較適合文本分析
    for word in words:
        if word.flag=="nr" and word.word in dict:
            dict[word.word]+=1
        elif word.flag =="nr" and word.word not in dict:
               dict[word.word]=1
print(dict)   
'''            
    
                
                
        

            
            
    
    
    

   
        
        
    


'''

import jieba
from jieba import posseg
'''

#import requests #requests 用 get
#import urllib.request 用 Request
