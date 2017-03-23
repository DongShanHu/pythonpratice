import pandas as pd
import urllib
import urllib.request
from bs4 import BeautifulSoup
import base64

url='http://www.tapmc.com.taipei/tapmc10/index_F0101sub.aspx'
pf=pd.read_html(url,encoding="UTF-8")

print(pf)
