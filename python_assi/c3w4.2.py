#c3w4.2.py by BANUKA VIDUSANKA

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL : ')
#if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html" #sample
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Ming.html" #quiz
count = int(input('Enter count: '))
position = int(input('Enter position: '))
    

for x in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    url = (tags[position-1]).get('href', None)
    name = (tags[position-1]).get('Contents:', (tags[position-1]).contents[0])
    print ('Retrieving:', url)
    
print('Name:', name)