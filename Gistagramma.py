import matplotlib.pyplot as plt


data = [1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 8, 8, 9, 10]


plt.hist(data, bins=10) # гистограмма плотности
# plt.scatter(x, y) # диаграмма рассеяния

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Тестовая гистограмма')

plt.show()