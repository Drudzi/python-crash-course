from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Dice are named for their number of sides... D6, D8, D10 and so on.
# Create a D6:
die = Die()

# Make some rolls and store results in a list:
results = []
for roll in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results:
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results:
#We'll make a histogram, showing how often certain results occur.

x_values = list(range(1, die.num_sides + 1)) 
#Plotly doesn't accept the results of the range func. directly so we make it a list.
data = [Bar(x=x_values, y=frequencies)]
#The Bar class represents a data set that will form a bar chart.
# Bar needs a set of x-values and y-values.
#  A Bar object should be wrapped in square brackets because a data set can have multiple elements.

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
#In plotly, each axis can be configured in multiple ways and configurations for an axis...
# should be stored in a dictionary. We only configure the title for this one.
my_layout = Layout(title='Results of rolling one D6 1000 times',
    xaxis=x_axis_config, yaxis=y_axis_config) #We insert the axis configs.

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
#offline.plot is used to generate the plot.
# It needs a dictionary containing the data and layout objects.
#  You can also specify a filename for the file where the graph will be saved.

#The file should open in a web browser.