# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Variables for the program
url = input('Enter - ')
cuenta = 0
nombres = list()

# Iterative repeater
while cuenta < 8:
    slate = list()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # RegEx to find the selected text in the url
    nombres.append(re.findall('[by][_](.+)[.]',url))

    # Retrieve all of the anchor tags
    for tag in tags:
        # Append in the slate
        slate.append(tag.get('href', None))
    
    # Update variables
    cuenta = cuenta + 1
    url = slate[17]
    continue

print(nombres)
