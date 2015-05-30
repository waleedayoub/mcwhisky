import requests
from lxml.html import fromstring
import sys
import time
  
url_pre = "http://whiskyadvocate.com/ratings-reviews/?brand_id=0&rating=0&price=0&category_id=0&issue_id=0&reviewer=0&page_num="

for page in xrange(1, 235):
    try:
        out = "-> On page {} of {}...        {}%"
        print out.format(page, "235", str(round(float(page)/235/100, 2)))
        resp = requests.get(url_pre + str(page))
        tree = fromstring(resp.text)
        reviews = tree.xpath('//div[(@class="table-container")]/text()')

        for item in reviews:
            print item.encode('utf-8')

        sys.stdout.flush()
        time.sleep(2)
    except:
        continue


# run these bash commands after to clean the file
grep -E -v '^-' whisky1.txt > whisky2.txt
sed '/^[[:space:]]*$/d;s/[[:space:]]*$//' whisky2.txt > whisky3.txt
sed 's/^/BEGIN NOW /' whisky3.txt > whisky4.txt
sed 's/$/ END/' whisky4.txt > whisky_final.txt