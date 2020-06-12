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
x_values = list(range(2, max_result+1))

#Visualize results:
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(x=x_values, bins=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], data=frequencies)

plt.show()