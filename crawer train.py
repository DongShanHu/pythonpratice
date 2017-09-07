import requests
from bs4 import BeautifulSoup

payload ={

"FromStationName":"1011",
"ToCity":"4",
"ToStation":"1317",
"ToStationName":"0",
"TrainClass":"2",
"searchdate":"2017-07-11",
"FromTimeSelect":"0000",
"ToTimeSelect":"2359",
"Timetype":"1",

    }
res=requests.post("http://twtraffic.tra.gov.tw/twrail/TW_SearchResult.aspx",data =payload)

#print(res.text)

soup=BeautifulSoup(res.text,'html.parser')

print(soup.title.string)
