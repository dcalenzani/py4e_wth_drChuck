import json
import urllib.request, urllib.parse, urllib.error
import ssl
x = 0

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#html data parsing
url = input('URL: ')
redurl = urllib.request.urlopen(url, context=ctx)
print('>>>>>>>>RETRIEVING ', url, '>>>>>>>>>>>>')

#json data extraction
data = redurl.read()
info = json.loads(data)
print('user count:', len(info))

#items
for item in info['comments']:
      x = x + item['count']

print(x)
