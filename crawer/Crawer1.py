import re
import urllib

request = urllib.Request("http://blog.marsw.tw")
response = urllib.urlopen(request)
html = response.read()
print(html)

fileout = file("01_blog.html","w")
fileout.write(html)
fileout.close()
