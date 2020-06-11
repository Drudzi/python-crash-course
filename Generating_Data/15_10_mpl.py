#Let's visualize dice rolls using matplotlib and a histogram.

import matplotlib.pyplot as plt

from die import Die

# Create two D6 dice:
die_1 = Die()
die_2 = Die()

# Roll the dice and get the results:
results = [die_1.roll() + die_2.roll() for roll in range(10_000)]

# Analyze results:
max_result = die_1.roll() + die_2.roll()
frequencies = [results.count(value) for value in range(2, max_result+1)]

#Visualize results:
x_values = list(range(2, max_result+1))