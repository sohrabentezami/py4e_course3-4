import urllib.request, urllib.parse, urllib.error
import json
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(data)
#print('User count:', len(info))

for item in info['comments']:
    print('Name', item['name'])
    
