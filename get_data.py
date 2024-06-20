import requests
import os


# Получение данных
data = 'https://archive.ics.uci.edu/static/public/186/data.csv'
response = requests.get(data, verity=False)

os.makedirs('data', exist_ok=True)

# Сохранение в файл
with open('data/wine.csv', 'wb') as file:
    file.write(response.content)