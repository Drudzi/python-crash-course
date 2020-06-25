import matplotlib.pyplot as plt

#   Plotting and styling individual points with scatter():
#Sometimes you want to plot individual points based on certain characteristics.
# You might for an example, want to plot small values in one color and larger values in another color.

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(2, 4, s=200)
#scatter() plots a single point at a given value. (x, y) is required.
# Param. s set the size of the dot.

# Set chart title and label axes:
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Vaule", fontsize=14)

# Set size of tick labels:
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()