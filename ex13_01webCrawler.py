import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import os

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

#clear_screen()

### Ignor SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url-')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/known_by_Brendyn.html'
t2 = int(input('Link pos: '))
t2 = t2-1
count = int(input('Enter count: '))
print('Retrieving: ', url)


while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read() ##reads the file as a hole and adds the ssl cert ignor
    soup = BeautifulSoup(html, 'html.parser') #creats the soup
    tags = soup('a')   ## looks for a tags asin link anchors
    adline = str(tags[t2])   ##reads the link pos tab
    sline = adline.split('"')
    print('Retrieving: ', sline[1])  
    url = sline[1]
    count = count - 1


##retriving the ahncor tags
#tags = soup('a')  # looks for all the a tags in soup(the parsed page)
#for tag in tags[:3]:    # hops threw the tags
    #print('TAG:', tag)
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    #print('')
