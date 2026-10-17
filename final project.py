import requests
from bs4 import BeautifulSoup

url = "https://store.steampowered.com/search/?category1=998"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    games = soup.find_all('a', {"class": 'search_result_row'})

    print("Назви та оцінки відеоігор:\n")

    for game in games[:10]:
        title = game.find('span', {"class": 'title'})
        rating = game.find('span', {"class": 'search_review_summary'})

        if title:
            print("Гра:", title.text.strip())

            if rating:
                print("Оцінка:", rating.get('data-tooltip-html', 'Немає оцінки'))
            else:
                print("Оцінка: Немає оцінки")

            print()
else:
    print("Сторінку не вдалося завантажити")