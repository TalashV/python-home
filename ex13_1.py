from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
lst = list()
tags = soup('span')
for tag in tags:
#    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0].contents[0])
 #   print('Attrs:', tag.attrs)
    #lst.append(int(tag.contents[0]))
#print (sum(lst))