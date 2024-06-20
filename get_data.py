import requests

# Получение данных
data = 'https://archive.ics.uci.edu/static/public/186/data.csv'
response = requests.get(data)

# Сохранение в файл
with open('data/wine.csv', 'wb') as file:
    file.write(response.content)