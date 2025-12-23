import matplotlib.pyplot as plt

h1 = [150, 155, 160]
w1 = [50, 55, 60]

h2 = [165, 170, 175]
w2 = [65, 70, 75]

h3 = [180, 185, 190]
w3 = [80, 85, 90]

plt.scatter(h1, w1)
plt.scatter(h2, w2)
plt.scatter(h3, w3)

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")
plt.show()
