#c3w5.py
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_850579.json"
print("Retrieving:", url)
    
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
#tree = ET.fromstring(data)

info = json.loads(data)
#print('Comment countTot:', len(info))
#print(info)
totsum = 0
totcount = 0
#print("============")
for item in info['comments']:
    totsum = totsum + int(item['count'])
    totcount = totcount + 1
    
print("Count:", totcount,"\nSum:", totsum )
