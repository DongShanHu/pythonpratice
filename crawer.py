import requests as re
res = re.get("https://www.youtube.com/watch?v=5yAU52qfYuU")

m=re.search ('"args":({.*?}),',res.text)

##print (res.text)
print(m.group(1))
