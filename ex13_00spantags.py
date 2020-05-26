import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

### Ignor SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    url = input('Enter url-')
    if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.html'
    try:
        html = urllib.request.urlopen(url, context=ctx).read() ##reads the file as a hole and adds the ssl cert ignor
        break
    except:
        print('Not a valid url')
        continue
    
soup = BeautifulSoup(html, 'html.parser') #creats the soup

lst = list()
##retriving the ahncor tags
tags = soup('span')  # looks for all the a tags in soup(the parsed page)
for tag in tags:    # hops threw the tags
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    num = tag.contents[0]
    lst.append(int(num))
print(sum(lst))