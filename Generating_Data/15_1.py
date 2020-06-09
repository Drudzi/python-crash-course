import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=5)
ax.axis([0, 5250, 0, 1.3*10**11])

# Set chart title and label axes:
ax.set_title("Cube Numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=13)
ax.set_ylabel("Cube of Value", fontsize=13)
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()