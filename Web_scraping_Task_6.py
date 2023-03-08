'''TASK 6: FROM THE COMPLETE PYTHON BOOTCAMP FROM ZERO TO HERO BY JOSE PORTILLA
Notice how there is more than one page, and subsequent pages look like this
http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation
to loop through all the pages and get all the unique authors on the website. Keep in mind there
are many ways to achieve this, also note that you will need to somehow figure out how to check that
your loop is on the last page with quotes. For debugging purposes, I will let you know that there
are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a
loop that is robust enough that it wouldn't matter to know the amount of pages beforehand,
perhaps use try/except for this, its up to you!
'''

import requests
import bs4

authors = set()

n = 1
website = f'http://quotes.toscrape.com/page/{n}/'
result = requests.get(website).text
is_page = 'Next' in result
while is_page == True:
    website = f'http://quotes.toscrape.com/page/{n}/'
    result = requests.get(website).text
    soup = bs4.BeautifulSoup(result, 'lxml')
    all_authors = soup.select('.author')
    # print(f'page {n}: ', all_authors)
    for author in all_authors:
        authors.add(author.text)
    n += 1
    is_page = 'Next' in result
    # print(is_page)
print(authors)

