# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
import scrapy

driver = webdriver.Chrome()
url = 'https://www.divan.ru/category/divany-i-kresla'
driver.get(url)

# Ожидание загрузки страницы
time.sleep(5)  # Лучше использовать WebDriverWait для более надежного ожидания


# Поиск элементов с ценами (замените селектор на актуальный)
price_elements = driver.find_elements(By.XPATH, '//span[@data-testid="price"]/#text')

# Закрытие веб-драйвера
driver.quit()

# Извлечение цен
prices = [price.text for price in price_elements]

# Сохранение в CSV файл
with open('prices_Divans.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовок столбца

    # Запись цен в CSV файл
    for price in prices:
        writer.writerow([price])




