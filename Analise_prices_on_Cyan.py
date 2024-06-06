from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


driver = webdriver.Chrome()

url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver.get(url)

# Ожидание загрузки страницы
time.sleep(5)  # Лучше использовать WebDriverWait для более надежного ожидания



# Поиск элементов с ценами (замените селектор на актуальный)
price_elements = driver.find_elements(By.CSS_SELECTOR, 'span[@data-mark="MainPrice"]/span')

# Извлечение цен
prices = [price.text for price in price_elements]

# Сохранение в CSV файл
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовок столбца

    # Запись цен в CSV файл
    for price in prices:
        writer.writerow([price])


# Закрытие браузера
driver.quit()

