# -*- coding: utf-8 -*-
"""
@author: 通識中心 施孟賢
"""
import requests
from bs4 import BeautifulSoup

#pip install jieba
#import jieba.posseg # https://github.com/fxsjy/jieba

def ptt_scraping(url):
    articles = []
    r = requests.get(url=URL, cookies={"over18":"1"})
    soup = BeautifulSoup(r.text, "lxml")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        if tag.find("a"):
            href = tag.find("a")["href"]
            title = tag.find("a").text
            
            r2=requests.get(url="http://ptt.cc"+href, cookies={"over18":"1"})
            soup2 = BeautifulSoup(r2.text, "lxml")

# New script to add date information of the PTT article
            meta_spans = soup2.find_all("span", class_="article-meta-value")
            try:
                date_span = meta_spans[-1]
                
                text = "\n".join(soup2.text.split("\n"))
                articles.append({"title":title, "href":href, "text":text, "date": date_span.text})
            except:
                pass
    return articles

#pip install jieba
import jieba.posseg # https://github.com/fxsjy/jieba
import os, time

board = "Gossiping"
#board = "C_Chat" # 5/15 -> C_Chat/index9966.html 雙北升3級; 5/19 -> C_Chat/index10050.html 全國3級.
if board not in os.listdir("."):    
    os.mkdir(board)


for i in range(30000,30050): 

    # TODO: change this code
    URL = "https://www.ptt.cc/bbs/%s/index%d.html" % (board, i) 
    print("Crawling URL", URL)

    articles = ptt_scraping(url=URL)

    for article in articles[:3]:    
        
        filename = article["href"].split("/")[-1]
        print("full-href", URL[:13] + article["href"])
        
        directory = article["date"]
        path = board + "/" + directory[:10]
        if directory[:10] not in os.listdir(board):
            os.mkdir(path = path)

        with open(file="%s/%s.txt" % (path,filename), mode="w", encoding="utf8") as file1:
            tagged_words = jieba.posseg.cut(article["text"])
            words = [word for word, pos in tagged_words if pos not in ['m']]
            file1.write(article["date"]+"\n")
            file1.write(" ".join(words))
            print(article["date"], " ".join(words).strip()[:22])
        
    time.sleep(3)