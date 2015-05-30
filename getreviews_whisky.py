import requests
from lxml.html import fromstring
import sys
import time
  
url_pre = "http://whiskyadvocate.com/ratings-reviews/?brand_id=0&rating=0&price=0&category_id=0&issue_id=0&reviewer=0&page_num="

for page in xrange(1, 262):
    try:
        out = "-> On page {} of {}...        {}%"
        print out.format(page, "235", str(round(float(page)/262/100, 2)))
        resp = requests.get(url_pre + str(page))
        tree = fromstring(resp.text)
        reviews = tree.xpath('//div[(@class="review")]/text()')

        for item in reviews:
            print item.encode('utf-8')

        sys.stdout.flush()
        time.sleep(2)
    except:
        continue