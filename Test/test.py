from urllib.request import urlopen
html = urlopen("http://www.yahoo.com.tw/")
s=html.read()
print(s)
