<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup


for i in range(100,1,-1):
        res=requests.get('https://www.ptt.cc/bbs/Tennis/index{0}.html'.format(i),verify=True)
        soup=BeautifulSoup(res.text)
        for entry in soup.select(".r-ent"):
            print(entry.select(".title")[0].text.strip())

=======
import requests
from bs4 import BeautifulSoup


for i in range(100,1,-1):
        res=requests.get('https://www.ptt.cc/bbs/Tennis/index{0}.html'.format(i),verify=True)
        soup=BeautifulSoup(res.text)
        for entry in soup.select(".r-ent"):
            print(entry.select(".title")[0].text.strip())

>>>>>>> e43e6f22ec50c96d77281abd0092d9d0a672b730
