import requests
from lxml.html import fromstring
import sys
import time
  
url_pre = "http://whiskyadvocate.com/ratings-reviews/?brand_id=0&rating=0&price=0&category_id=0&issue_id=0&reviewer=0&page_num="
  
# iterate through each page of reviews
page = requests.get(url_pre + str(1))
tree = fromstring(page.text)
reviews = tree.xpath('//div[(@class="review")]/text()')

# create lists of reviews
# reviews = tree.xpath('//div[@class="review"]/text()')

for item in reviews:
    print item.encode('utf-8')