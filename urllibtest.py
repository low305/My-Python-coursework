import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

### Ignor SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    url = input('Enter url-')
    try:
        html = urllib.request.urlopen(url, context=ctx).read() ##reads the file as a hole and adds the ssl cert ignor
        break
    except:
        print('Not a valid url')
        continue
soup = BeautifulSoup(html, 'html.parser') #creats the soup

##retriving the ahncor tags
tags = soup('a')  # looks for all the a tags in soup(the parsed page)
for tag in tags:    # hops threw the tags
    print(tag.get('href', None)) 
