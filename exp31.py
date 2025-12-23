import matplotlib.pyplot as plt
import random

x = [random.randint(1, 50) for _ in range(10)]
y = [random.randint(1, 50) for _ in range(10)]

plt.scatter(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Random Scatter Plot")
plt.show()
