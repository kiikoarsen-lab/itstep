import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    print("Назва сайту:", soup.title.text)

    books = soup.find_all('article', {"class": 'product_pod'})

    for book in books[:5]:
        title = book.find('h3').find('a')['title']
        price = book.find('p', {"class": 'price_color'})

        print("Назва:", title)
        print("Ціна:", price.text)
else:
    print('Сторiнку не вдалось завантажити')