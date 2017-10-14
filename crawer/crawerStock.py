import request
res =resquest.get('https://world.taobao.com/search/search.htm?cat=50005050&_ksTS=1489679860919_300&spm=a21bp.8294643.banner_cat.411.RaxXU5&_input_charset=utf-8&navigator=all&json=on&cna=rBeuEAnF6gsCAW%2F5GPnTVG57&callback=__jsonp_cb&abtest=_AB-LR517-LR854-LR895-PR517-PR854-PR895')
print (res.text)



'''
import request
from bs4 import BeautifulSoup
import base64
payload ={}
res=resquest.get('http://www.tse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_d.php')
res.encoding='big5'
soup=BeautifulSoup(res.text)
for inp in soup.select('input'):
    if'hidden' in inp.get('type'):
        payload[inp.get('name')].base64.b64encode(inp.get('value').encode('utf-8'))

res2=requests.post('http://www.tse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_print.php?language=ch&save=csv')

from shutil import copyfileobj
f=open('export.csv','desktop')
copyfileobj(res2.raw,f)
f.close()

##print payload
            
'''
