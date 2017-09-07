import requests
from bs4 import BeautifulSoup
import lxml

url="https://www.ptt.cc/bbs/Beauty/index.html"
for i in range(3):
    res=requests.get(url)
    
    soup=BeautifulSoup(res.text,"lxml")
    
    articles=soup.select('div.title a')

    paging=soup.select('div.btn-group-paging a')
    
    next_url="http://www,ptt,cc"+paging[1]['href']
    
    url=next_url

    for article in articles:
        print(article.text,article['href'])
