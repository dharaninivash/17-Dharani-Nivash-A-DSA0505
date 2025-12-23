import matplotlib.pyplot as plt

# Data
lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Bar chart with different colors
plt.bar(lang, pop, color=['r', 'g', 'b', 'y', 'c', 'm'])
plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("Programming Language Popularity")
plt.show()
