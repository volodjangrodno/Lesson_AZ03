import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Parabola')

plt.grid(True) # включить сетку

plt.show()