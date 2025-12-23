import matplotlib.pyplot as plt
import random

x = [random.randint(1, 50) for _ in range(10)]
y = [random.randint(1, 50) for _ in range(10)]
sizes = [i * 50 for i in range(10)]

plt.scatter(x, y, s=sizes)
plt.title("Scatter Plot with Different Sizes")
plt.show()
