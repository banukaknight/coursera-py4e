#c3w5.py
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_850578.xml"
print("Retrieving:", url)
    
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')
totsum = 0
totcount = 0
for item in lst:
    totsum = totsum + int(item.find('count').text)
    totcount = totcount + 1
    
print("Count:", totcount,"\nSum:", totsum )