import requests 
from bs4 import BeautifulSoup
import urllib.request# url request
import os
import datetime
link='https://www.treasury.gov/ofac/downloads/alt.ff'
link2='https://www.treasury.gov/ofac/downloads/sdn.ff'


target_url = "https://www.treasury.gov/resource-center/sanctions/SDN-List/Pages/sdn_data.aspx"
rs = requests.session()
res = rs.get(target_url, verify=False,allow_redirects=True)
soup = BeautifulSoup(res.text, 'html.parser')
content = ""
# print(soup)


for data in  soup.select('div.article-date'):
    title = data.text
#     link =data['href']
    content=title.lstrip()
# print(content)

today_date = datetime.date.today()+datetime.timedelta(days=-1)
new_today_date = today_date.strftime("%m/%d/%Y")


if new_today_date[0] !=1 :
    new_today_date=new_today_date[1:10]
else:
    new_today_date=new_today_date
    
if new_today_date==content:
    urllib.request.urlretrieve(link, os.path.join('./SDN.FF'))
    urllib.request.urlretrieve(link2, os.path.join('./ALT.FF'))
    print("download OFAC blacklist")
