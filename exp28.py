import matplotlib.pyplot as plt

# Data
lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Horizontal bar chart
plt.barh(lang, pop)
plt.xlabel("Popularity")
plt.ylabel("Programming Languages")
plt.title("Popularity of Programming Languages")
plt.show()
