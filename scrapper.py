from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# my_url = 'https://www.canadacomputers.com/index.php?cPath=7_4527&sf=:&co=&mfr=&pr=1000-1499.99' # confirmed you can scrape canada computers
# my_url = 'https://www.bestbuy.ca/en-ca/search?search=desktop'

# uClient = uReq(my_url) # returns raw HTML of URL

# page_html = uClient.read()

# uClient.close()

# page_soup = soup(page_html, "html.parser") # parses html

# # products = page_soup.findAll("article", {"class":"product_pod"}) # Holds all the products on the page in a list
# title = page_soup.head.title
# print(title)

# filename = 'books.csv'
# f = open(filename, "w")
# headers = "title, price\n"
# f.write(headers)

# for product in products:
#     title = product.h3.a["title"] # grabs the title of the book
#     price = product.select('div')[1].p.get_text() # grabs price

#     f.write(title.replace(",", "|") + "," + price.replace(",", "|") + "\n") # replace , with anything to avoid csv error

# f.close

