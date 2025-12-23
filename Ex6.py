import matplotlib.pyplot as plt

price = [100, 102, 105]
volume = [3000, 5000, 4000]

plt.scatter(price, volume)
plt.xlabel("Price")
plt.ylabel("Volume")
plt.title("Price vs Volume")
plt.show()
