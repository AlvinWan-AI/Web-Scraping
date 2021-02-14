from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import os
import re
import requests
import csv

myurl = "https://www.yelp.ca/biz/pai-northern-thai-kitchen-toronto-5?osq=Restaurants"
html = urlopen(myurl).read()
soupified = bs(html, 'html.parser')

name = soupified.find('h1')
print(name.get_text().strip())
# Pai Northern Thai Kitchen

num_reviews = soupified.find('span', {
                             'class': "text__373c0__2Kxyz text-color--white__373c0__22aE8 text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--large__373c0__3t60B"})
print(num_reviews.get_text().strip())

allreview = soupified.find_all(
    "li", {'class': 'margin-b5__373c0__2ErL8 border-color--default__373c0__3-ifU'})

l = {}
u = []
for i in range(0, len(allreview)):
    l['name'] = allreview[i].find(
        'a', {'class':  'link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}).text
    l['address'] = allreview[i].find('span', {
                                     'class': 'text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-'}).text
    l['No. of friends'] = allreview[i].find(
        'span', {'class': 'text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe'}).text
    l['No. of reviews'] = allreview[i].find(
        'span', {'class': 'text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe'}).text
    l['Date'] = allreview[i].find('span', {
                                  'class': 'text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa-'}).text
    l['Review'] = allreview[i].find(
        'p', {'class': 'text__373c0__2Kxyz comment__373c0__1M-px text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-'}).text

    u.append(l)   # list of dictionary
    l = {}

if not os.path.exists('.\Yelp_Reviews'):
    os.mkdir('.\Yelp_Reviews')
filename = name.get_text().strip()
fname = f'Yelp_Reviews/{filename}.txt'

with open(fname, "w") as f:
    # https://stackoverflow.com/questions/36965507/writing-a-dictionary-to-a-text-file/51849823
    print({name.get_text().strip(): u}, file=f)

print(f'File saved in directory {fname}')
