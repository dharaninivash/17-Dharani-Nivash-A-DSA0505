import matplotlib.pyplot as plt

men = [22, 30, 35, 35, 26]
women = [25, 32, 30, 35, 29]

men_sd = [4, 3, 4, 1, 5]
women_sd = [3, 5, 2, 3, 3]

plt.bar(range(5), men, yerr=men_sd, label='Men')
plt.bar(range(5), women, bottom=men, yerr=women_sd, label='Women')

plt.legend()
plt.title("Stacked Bar Plot")
plt.show()
