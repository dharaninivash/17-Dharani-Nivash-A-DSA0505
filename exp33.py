import matplotlib.pyplot as plt
import random

x = [random.randint(1, 50) for _ in range(10)]
y = [random.randint(1, 50) for _ in range(10)]

plt.scatter(x, y, facecolors='none', edgecolors='blue')
plt.title("Empty Circle Scatter Plot")
plt.show()
