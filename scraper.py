import urllib.request
from bs4 import BeautifulSoup
import csv
import ssl

file_name = str(input('Enter output filename. Remember .csv '))

ssl._create_default_https_context = ssl._create_unverified_context
#needs ssl handshake

pageNumber = 0
lastPage = 6 #enter last pagenumber

# Write csv headers before scraping
with open(file_name, 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["stars", "headline", "full_review"])

while pageNumber <= lastPage:
    pageNumber = pageNumber + 1
    print('youre at pagenumber: ',pageNumber) #status in command line
    #enter amazon link with same format as:
    url = 'https://www.amazon.com/Yale-Assure-Button-Polished-YRD216NR605/product-reviews/B071CNVC2Z/ref=cm_cr_dp_d_acr_sr?ie=UTF8&reviewerType=' + str(pageNumber)

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
        with open(file_name, 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([stars, headline, full_review])
