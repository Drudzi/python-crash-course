import matplotlib.pyplot as plt

#   Plotting and styling individual points with scatter():
#Writing lists of data by hand can be very inefficient a lot of times.
# Rather than passing values to a list, it's more efficient to use a loop that does calculations for us.

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
#List comprehensions are effective for these types of calculations.
# It combines a for loop and the creation of...
#  new elements, and automatically appends each new element.

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
#scatter() can also plot a series of points.
# Then we pass it separate lists of x- and y-values.
#  Matplotlib reads one value from each list as it plots each point...
#   giving (1,1) (2, 4) (3, 9) etc.
#    It's appropriate to use a smaller dot size for larger data sets like this one.
#     c parameter defines the color of the dots. ex) Do c='red' to make dots red.
#      
#      With cmap you can assign the plot a colormap, a series of colors in a gradient.
#       We pass the y-values to c to base the gradient on the y values.
#        cmap assings which gradient to use. Blues gives small values a lighter blue and larger values a darker blue.

# Set chart title and label axes:
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Vaule", fontsize=14)

# Set size of tick labels:
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis:
ax.axis([0, 1100, 0, 1100000])
#axis() method specifies range for each axis.
# Requires for values, the min and max for the x- and y-axis.

plt.show()

#   Saving your plots automatically:
#If you want to save your plot to a file, replace plt.show() with a plt.savefig() call.

# plt.savefig('filename.png', bbox_inches='tight')

# bbox_inches argument reduces extra whitespace from the plot, not required.