import ssl
import json
import urllib.request, urllib.parse, urllib.error

 #api key setup
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#setup location South Federal University
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    add = dict()
    add['address'] = address
    if api_key is not False: add['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(add)

#decode new url
    print('Retrieving ', url)
    urlred = urllib.request.urlopen(url, context=ctx)
    data = urlred.read().decode()
    print('RETRIEVED ', len(data), 'characters')

    try:
        js = json.loads(data)
    #separar al id
        for item in js['results']:
            print('Your place_id is: ', item['place_id'])
            break
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('FAILURE')
        continue
    break
print('thanks for using our service')
