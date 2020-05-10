from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.ua-football.com/sport')
# print(req) # <http.client.HTTPResponse object at 0x02A6B9B8>
html = req.read()
# print(html)
soup = BeautifulSoup(html, 'html.parser') # парсим html-страницу
# print(soup) # выводит исходный код страницы

# выведем список новостей
news = soup.find_all('li', class_='liga-news-item')
# print(news)

results = []

for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True) # find() ищет только один элемент
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    href = item.a.get('href')
    # добавляем данные в словарь
    results.append({
        'title': title,
        'desc': desc,
        'href': href
    })

# print(results)

# запишем данные в файл
f = open('news.txt', 'w', encoding='utf-8')
i = 1 # счетчик, номер новости
for item in results:
    f.write(f"Новость № {i}\n\nНазвание: {item['title']}\nОписание: {item['desc']}\nСсылка: {item['href']}\n\n **********\n\n")
    i += 1
f.close()