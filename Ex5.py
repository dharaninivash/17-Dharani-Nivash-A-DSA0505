import matplotlib.pyplot as plt

dates = ["Day1","Day2","Day3"]
volume = [3000, 5000, 4000]

plt.bar(dates, volume)
plt.xlabel("Date")
plt.ylabel("Volume")
plt.title("Trading Volume")
plt.show()
