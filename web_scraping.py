#Libraries
import requests
import bs4
#Differents modes
mode = input ('1. first page authors \n2. first page quotes \n3. top ten tags \n4.unique authors \n Select:  ')
#Use libraries to connect
url = 'http://quotes.toscrape.com/'
result = requests.get (url)
soup = bs4.BeautifulSoup(result.text, 'lxml')
#Get the names of all authors of first page
if mode == 1:
    authors = soup.select('small.author')

    list_of_authors = []
    for author in authors:
        list_of_authors.append(author.getText())
    print (list_of_authors)

#Create a list of all quotes of the first page
elif mode ==  2:
    quotes = soup.select('.text')
    list_of_quotes = []
    for quote in quotes:
        list_of_quotes.append(quote.getText())
    print (list_of_quotes)

#Extract the top ten tags
elif mode == 3:
    tags = soup.select('.tag-item')

    for tag in tags:
        print (tag.getText())
#Loop through all the pages and get all the unique authors on the website
else: 
    url = 'http://quotes.toscrape.com/page/{}/'
    list_of_unique_authors = []
    page = 0
    while True: 
        page += 1
        result = requests.get (url.format(page))
        soup = bs4.BeautifulSoup(result.text, 'lxml')

        if 'No quotes found!' in soup.text:
            break
        authors = soup.select('.author')
        for author in authors:
            if author.getText() not in list_of_unique_authors:
                list_of_unique_authors.append(author.getText())
            else:
                continue
    number_authors = 0        
    for author in list_of_unique_authors:
        number_authors += 1
        print (f'{number_authors} {author}')