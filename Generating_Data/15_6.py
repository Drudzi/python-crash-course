from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D8 dice:
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls and store results in a list:
results = []
for roll in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results:
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results:
#We'll make a histogram, showing how often certain results occur.

x_values = list(range(2, max_result+1)) 
#Plotly doesn't accept the results of the range func. directly so we make it a list.
data = [Bar(x=x_values, y=frequencies)]
#The Bar class represents a data set that will form a bar chart.
# Bar needs a set of x-values and y-values.
#  A Bar object should be wrapped in square brackets because a data set can have multiple elements.

x_axis_config = {'title': 'Result', 'dtick': 1} #dtick controls spacing between tick marks. A value of 1 marks every bar.
y_axis_config = {'title': 'Frequency of Result'}
#In plotly, each axis can be configured in multiple ways and configurations for an axis...
# should be stored in a dictionary.
my_layout = Layout(title='Results of rolling two D8 dice 50.000 times',
    xaxis=x_axis_config, yaxis=y_axis_config) #We insert the axis configs.a

offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
#offline.plot is used to generate the plot.
# It needs a dictionary containing the data and layout objects.
#  You can also specify a filename for the file where the graph will be saved.

#The file should open in a web browser.