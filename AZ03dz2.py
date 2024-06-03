# 2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.


import matplotlib.pyplot as plt
import numpy as np

random_array1 = np.random.rand(15)  # массив из 15 случайных чисел
print(random_array1)
random_array2 = np.random.rand(15)
print(random_array2)

plt.scatter(random_array1, random_array2)
plt.show()