import matplotlib.pyplot as plt

dates = ['10-03','10-04','10-05','10-06','10-07']
close = [772,776,776,776,775]

plt.plot(dates, close)
plt.title("Alphabet Inc Stock")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.show()
