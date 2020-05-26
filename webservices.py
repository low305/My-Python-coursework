import xml.etree.ElementTree as ET  ##imports xml parser
import ssl
import urllib.request, urllib.parse, urllib.error

### Ignor SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location:')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_499378.xml'
print('Retreiving:', url)

#below uses the url lib 
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data) ## pass data into fromstring
comen = tree.findall('comments/comment') ## using .findall to creat a list of the tags
print('Count:', len(comen))             ## and looks for all the comment tags in the comments tags

lst = list()
for item in comen:
    x = int(item.find('count').text)
    lst.append(x)
print('Sum:', sum(lst))

#for item in lst: ## iterates through lst of user tags calling them item each time
    #print('Name:', item.find('name').text)  ## call .find() and .text on the name tag
    #print('Count:', item.find('count').text)      ## as above on the id tag
    #print('Attribute:', item.get("x"))     ## uses .get to get the attribute from x in user tags
    #print('')
