# Exercises from The Python bootcamp from zero to hero by Jose Portilla

# Task 1: Import any libraries you think you'll need to scrape a website.

import requests
import bs4


# Task 2: Use requests library and BeautifulSoup to connect to
# http://quotes.toscrape.com/ and get the HMTL text from the homepage.

result = requests.get('http://quotes.toscrape.com')
result_text = result.text
soup = bs4.BeautifulSoup(result_text, 'lxml')
print(soup)

# Task 3: Get the names of all the authors on the first page.
authors = set()

for name in soup.select(".author"):
    authors.add(name.text)

print(authors)

# Task 4: Create a list of all the quotes on the first page.
quotes = []

for single_quote in soup.select(".text"):
    quotes.append(single_quote.text)

print(quotes)

# Task 5: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests
# text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...).
# HINT: Keep in mind there are also tags underneath each quote,
# try to find a class only present in the top right tags, perhaps check the span.

tags_container = soup.select('.col-md-4')
# print(tags_container)

for tag_container in tags_container:
    print(tag_container.text)




