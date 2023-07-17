import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Insert URL
serviceurl = "https://py4e-data.dr-chuck.net/comments_42.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Json
url='http://python-data.dr-chuck.net/comments_42.json'
uh= urllib.request.urlopen(url).read()
info =json.loads(uh)
count_values = [ el['count'] for el in info['comments'] ]
name_values = [ el['name'] for el in info['comments'] ]
print(count_values)
print(name_values)
