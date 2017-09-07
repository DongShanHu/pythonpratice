import requests
from bs4 import BeautifulSoup
import pandas as pd

#爬出全部內容
res=requests.get("http://search.books.com.tw/search/query/key/python/cat/all")

#爬出tiltle
soup=BeautifulSoup(res.text,'html.parser')
print (soup.title.string)

#爬取書名
books=pd.Series()
for book in soup.select("img[class='itemcov']"):
    books =books.append(pd.Series([book['alt']])).reset_index(drop=True)


#爬取定價
#i=0
#prices=pd.Series()
#for tag in soup.select('b'):
 #   if i%2==1 and i/2<books.size:
  #      prices=prices.append(pd.Series([tag.string])).reset_index(drop=True)
   #     i+=1


#爬取價格
i = 0
prices = pd.Series()
for price in soup.select("span[class='price']"):
    if(i<books.size):
        if(len(price.select('b'))==1): #只有價格
            prices = prices.append(pd.Series([price.select('b')[0].string])).reset_index(drop=True) # .string取tag<b>中的文字內容
        elif(len(price.select('b'))==2): #有打折數+價格
            prices = prices.append(pd.Series([price.select('b')[1].string])).reset_index(drop=True,) # .string取tag<b>中的文字內容
        else:
            break
    i+=1

#合併成DataFrame
df=pd.DataFrame({'書名':books ,'價格':prices})
print(df[['書名','價格']],axis=1)

