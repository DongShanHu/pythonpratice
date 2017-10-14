<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup



##url="https://www.ptt.cc/bbs/Beauty/index.html"
##for i in range(3):
##    res=requests.get(url)
##    
##    soup=BeautifulSoup(res,"html-parser")
##    
##    articles=soup.select('div.title a')
##
##    paging=soup.select('div.btn-group-paging a')
##    
##    next_url="http://www,ptt,cc"+paging[1]['href']
##    
##    url=next_url
##
##    for article in articles:
##        print(article.text,article['href'])

for i in range(3528,3519,-1):
    res=requests.get('https://www.ptt.cc/bbs/Beauty/index{0}.html'.format(i),verify=True)
    soup=BeautifulSoup(res.text)
    for entry in soup.select('.r-ent'):
        print(entry.select(".tltle")[0].text.strip())
=======
import requests
from bs4 import BeautifulSoup



##url="https://www.ptt.cc/bbs/Beauty/index.html"
##for i in range(3):
##    res=requests.get(url)
##    
##    soup=BeautifulSoup(res,"html-parser")
##    
##    articles=soup.select('div.title a')
##
##    paging=soup.select('div.btn-group-paging a')
##    
##    next_url="http://www,ptt,cc"+paging[1]['href']
##    
##    url=next_url
##
##    for article in articles:
##        print(article.text,article['href'])

for i in range(3528,3519,-1):
    res=requests.get('https://www.ptt.cc/bbs/Beauty/index{0}.html'.format(i),verify=True)
    soup=BeautifulSoup(res.text)
    for entry in soup.select('.r-ent'):
        print(entry.select(".tltle")[0].text.strip())
>>>>>>> e43e6f22ec50c96d77281abd0092d9d0a672b730
