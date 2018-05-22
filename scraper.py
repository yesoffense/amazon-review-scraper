import urllib.request
from bs4 import BeautifulSoup
import csv
import ssl
import time
import random

ssl._create_default_https_context = ssl._create_unverified_context
#needs ssl handshake

pageNumber = 0
lastPage = #enter last pagenumber at review site

browser_agents = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Mwendo/1.1.5 Safari/537.21",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4",
    "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"
]

browser_agent = random.choice(browser_agents)

# Write csv headers before scraping
with open('output_filename.csv', 'a') as csv_file: #you could enter different output filename. remember to do the same in line 56. remember .csv
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["stars", "headline", "full_review"])

while pageNumber <= lastPage:
    pageNumber = pageNumber + 1
    print('youre at pagenumber: ',pageNumber) #status in command line
    #enter amazon link with same format as:
    url = 'https://www.amazon.com/Haribo-Gold-Bears-Original-5-Pound-Packaging/product-reviews/B000EVOSE4/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(pageNumber)
    req = urllib.request.Request(
        #.Request is a BS built-in function
        url,
        data = None,
        headers = {
            'User-Agent': browser_agent
        }
    )

    response_html = urllib.request.urlopen(req)
    #saves site in variable
    soup = BeautifulSoup(response_html, 'html.parser')
    time.sleep(1)

    for review in soup.find_all('div', attrs = {'class': 'review'}):
        stars = review.find('a', attrs = {'class': 'a-link-normal'}).text.strip()
        headline = review.find('a', attrs = {'class': 'review-title'}).text.strip()
        full_review = review.find('span', attrs = {'class': 'review-text'}).text.strip()
        print(headline)
        # open a csv file with append, so old data will not be erased
        with open('output_filename.csv', 'a') as csv_file: #you could enter different output filename. remember .csv
            print('writing')
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([stars, headline, full_review])
