import urllib2
from lxml.html import fromstring
import sys
import time
  
urlprefix = "http://whiskyadvocate.com/ratings-reviews/?brand_id=0&rating=0&price=0&category_id=0&issue_id=0&reviewer=0&page_num="
  
response = urllib2.urlopen(urlprefix + str(1))
html = response.read()
dom = fromstring(html)
sels = dom.xpath('//*[(@id = "content")]//p')
print html