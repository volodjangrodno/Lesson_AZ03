import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из очищенного CSV файла
df = pd.read_csv('clean_prices.csv')

# Предполагаем, что цены находятся в столбце с именем 'price'
prices = df['Price']

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=30, edgecolor='k', alpha=0.7)
plt.title('Гистограмма цен')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')

# Отображение графика
plt.show()