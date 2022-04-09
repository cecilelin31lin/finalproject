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
import jieba
import jieba.analyse #看看沒有他可不可以用open
import jieba.posseg as psg


def NOOB_crawling(url):
    request=req.Request(url, headers={"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}) #f12 headers是正常使用者在訪問網頁時會留下的資料，寫近來ip才不會被封鎖
    with req.urlopen(url) as response:
        data=response.read().decode(encoding="utf-8") #harry potter text gbk、ISO...、uft8無法解碼，怎麼辦?
    root=bs4.BeautifulSoup(data,"lxml") #lxml是在解析甚麼，印出來看起來跟utf8解出來一樣
    txts=root.find("pre", id="SourceText")
    return txts


jieba.load_userdict("userdict.txt")
dict={}
with open(file="harry_potter_s1_seg", mode="w", encoding="utf8") as file:
    for i in range(1,18):
        url="http://www.haodoo.net/?M=u&P=G1278:%d&L=book" %(i)
        for txt in NOOB_crawling(url):
            words=psg.cut(txt)
            
            stopwords=[]
            for stopword in open(file="stopwords.txt", mode="r", encoding="utf-8"):
                stopwords.append(stopword.strip())
            
            for word in words:
                if word not in stopwords:
                    file.write(" ".join(word))
                    if word.flag=="nr" and word.word in dict: #posseg.pair才可以用.flag
                        dict[word.word]+=1
                    elif word.flag =="nr" and word.word not in dict:
                        dict[word.word]=1        
        time.sleep(3)

names=list(dict.items())
names_sorted=names.sort(key=lambda x:x[1], reverse=True)
#print(names_sorted) #None?

    

        

#小結: jieba有成功的斷詞，但無法正確斷出人名
#     加自定義字典


'''
dict={}
with open(file="harry_potter_s1", mode="r", encoding="utf8") as file: #不是decoding喔!
#Python3的str 默認不是bytes，所以不能decode，只能先encode轉為bytes，再decode
#'builtin_function_or_method' object has no attribute 'decode' ????
    
    txt=file.readlines #讀取每行，到底需不需要，因為文本中有的沒有分行?
    words=psg.cut(txt) #cut_all=False 精確分析模式較適合文本分析
    for word in words:
        if word.flag=="nr" and word.word in dict:
            dict[word.word]+=1
        elif word.flag =="nr" and word.word not in dict:
               dict[word.word]=1
print(dict)   
'''           
'''
def remove_stop_words(file_name,seg_list):
  with open(file=file_name, mode='r', encoding="utf-8") as f:
    stop_words = f.readlines()
  stop_words = [stop_word.rstrip() for stop_word in stop_words]
  
  for seg in seg_list:
    if seg not in stop_words:
      new_list.append(seg) 
  return new_list
file_name = 'stopwords.txt'
seg_list = remove_stop_words(file_name,seg_list)
print('remove_stop_words: ',seg_list)


stopwords=[]
for word in open('stopwords.txt','r'):
stopwords.append(word.strip())
article=open('1.txt','r').read()
words=jieba.cut(article,cut_all=False)
stayed_line=""
for word in words:
if word.encode("utf-8")not in stopwords:
stayed_line =word " "
print stayed_line
w=open('2.txt','w')
w.write(stayed_line.encode('utf-8'))

'''
    
                
                
        

            
            
    
    
    

   
        
        
    


'''

import jieba
from jieba import posseg
'''

#import requests #requests 用 get
#import urllib.request 用 Request
