from bs4 import BeautifulSoup
from urllib.request import urlopen
myurl = "https://www.canadacomputers.com/product_info.php?cPath=4_64_1969&item_id=183427"
html = urlopen(myurl).read()
soupified = BeautifulSoup(html, "html.parser")
q = soupified.find('div', {'class': 'col-12 py-2'})
outofstock = q.find('div', {'class': 'pi-prod-availability'})
print(f'try: ', outofstock.get_text().strip())

# How can I check in 1) every 5 mins 2) any words change 3) notification
