#Let's visualize dice rolls using matplotlib and a histogram.

import matplotlib.pyplot as plt

from die import Die

# Create two D6 dice:
die_1 = Die()
die_2 = Die()

# Roll the dice and get the results:
results = [die_1.roll() + die_2.roll() for roll in range(10_000)]

# Analyze results:
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
x_values = list(range(2, max_result+1))

#Visualize results:
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(x_values, frequencies)
ax.set_xticks(x_values)
ax.set_title('Results of rolling two D6 dice 10.000 times', fontsize=20)
ax.set_xlabel('Result', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

plt.show()