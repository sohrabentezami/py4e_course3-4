# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print(url)
a = url.split('_')
b=a[2].split('.')
print(b[0])


# Retrieve all of the anchor tags
for i in range(7) :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[17].get('href', None)
    #print(url)
    a = url.split('_')
    b=a[2].split('.')
    print(b[0])

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
url = tags[0].get('href', None)
#print(url)
a = url.split('_')
b=a[2].split('.')
print(b[0])
