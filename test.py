import requests
import bs4



url = 'http://books.toscrape.com/catalogue/page-{}.html'



number = 0
for page in range (1,51):
    result = requests.get (url.format(page))
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if book.select('.star-rating.Two') != []:
            number += 1
            title = book.select('a')[1]['title']
            print (f'{number}. {title}')