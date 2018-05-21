import urllib.request
from bs4 import BeautifulSoup
import csv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
#needs ssl handshake

pageNumber = 0
lastPage = 3

# Write csv headers before scraping
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["stars", "headline", "full_review"])

while pageNumber <= lastPage:
    pageNumber = pageNumber + 1
    url = 'https://www.amazon.com/Coup-d%C3%89tat-Practical-Edward-Luttwak/product-reviews/0674175476/ref=cm_cr_arp_d_paging_btm_3?ie=UTF8&reviewerType=all_reviews%3FpageNumber%3D3&pageNumber=' + str(pageNumber)

    req = urllib.request.Request(
        #.Request is a BS built-in function
        url,
        data = None,
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    response_html = urllib.request.urlopen(req)
    #saves site in variable

    soup = BeautifulSoup(response_html, 'html.parser')

    for review in soup.find_all('div', attrs = {'class': 'review'}):
        stars = review.find('a', attrs = {'class': 'a-link-normal'}).text.strip()
        headline = review.find('a', attrs = {'class': 'review-title'}).text.strip()
        full_review = review.find('span', attrs = {'class': 'review-text'}).text.strip()

        # open a csv file with append, so old data will not be erased
        with open('index.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([stars, headline, full_review])
