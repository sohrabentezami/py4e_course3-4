import urllib.request, urllib.parse, urllib.error
import json
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()
tree =  ET.fromstring(data)
tags = tree.findall('comments/comment')
print(tags)

s = 0
for tag in tags :
    c = tag.find('count')
    s = s + int(c.text)
print(s)
