import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_1530753.xml'
count = list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#open URL for data extraction
link = urllib.request.urlopen(url)
data = link.read()

#Calling a tree transforms XML tags to strings and list tags
tree = ET.fromstring(data)

#find tags that match
counts = tree.findall('comments/comment/count')

for item in counts:
    num = int(item.text)
    count.append(num)
    #print(item.text)

print(sum(count))
