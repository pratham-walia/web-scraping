from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.amazon.in/s?k=sports+shoes+sneakers+men+adidas&rh=n%3A1983396031&ref=nb_sb_noss').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('scrape.csv', 'w')

csv_writer = csv.writer(csv_file)


for shoe in soup.find_all('div', class_='sg-col-20-of-24 s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16'):
    headline = shoe.find('div', class_= 'a-size-base-plus a-color-base')
    summary = shoe.find('div', class_='a-size-base-plus a-color-base a-text-normal')
    link = shoe.find('div', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    
    csv_writer.writerow([headline, summary, link])

csv_file.close()