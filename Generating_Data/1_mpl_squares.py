import matplotlib.pyplot as plt
#We import the pyplot library which allows us to generate charts and plots.

#   Plotting a simple line graph:
squares = [1, 4, 9, 16, 25] #A list of data to plot!
input_values = [1, 2, 3, 4, 5] #Corresponding values to squares.

plt.style.use('seaborn')
#To style your plots use style module. You can customize a lot of things like color and fonts.
# To see available styles, run plt.style.available in a terminal session.

fig, ax = plt.subplots()
#subplots() can generate one or more plots in the same figure.
# var fig represents all the plots that are generated.
#  var ax represents a single plot in the figure.

ax.plot(input_values, squares, linewidth=3)
#The plot() function tries to plot the given dataset in the most meaningful way.
# linewidth parameter controls the thickness of the generated line.
#  without any given input values, plot() will correspond the first value in squares with 0, but it should be 1.

# Set chart title and label axes:
ax.set_title("Square Numbers", fontsize=24) #set_title sets the title for the chart.
ax.set_xlabel("Value", fontsize=14) #set_xlabel sets the title for x-axis.
ax.set_ylabel("Square of Value", fontsize=14) #set_ylabel sets the title for y-axis.

# Set size of tick labels:
ax.tick_params(axis='both', labelsize=14)
# tick_params styles the tick marks.

plt.show()
#The show() function opens the matplotlib viewer and displays the plot.