import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 3, 3, 4, 6, 6, 7, 8, 10, 12]

plt.plot(x, y) # линейный график


plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My first graph!')

plt.show()