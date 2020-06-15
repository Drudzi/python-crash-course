from datetime import datetime
import csv
# The csv module is from the Python standard library and helps working with and reading csv files.
#  csv = comma-separated values

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) #We assign a csv.reader object to reader, which reads the csv.
    header_row = next(reader) #We skip the header row.

    # Get dates, and high and low temperatures from this file:
    dates, highs, lows = [], [], []
    for row in reader:        
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        #We use the datetime module and its strptime to convert the dates...
        # from string to an objects representing the dates.
        #  striptime() needs two arguments, the first one should be a string containing the date.
        #   The second argument should tell Python how the date is formatted.
        #    #See documentation or table 16-1.

        high = int(row[5])
        low = int(row[6])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        #Now, we have the max temps, low temps and the dates stored!

# Plot the high temperatures:
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6) #Without any input values (x), it starts off at 0. Dates contains our input values.
ax.plot(dates, lows, c='blue', alpha=0.6) #We make a new plot of the low temps. Alpha controls transparency.
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#fill_between is used to determine the range between datasets, and we'll give that area some color.
# It needs a set of x values and two sets of y values to fill the space between.
#  facecolor parameter controls the color of the region.
#   This shading helps the range between the data sets become more apparent.

# Format plot:
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() #autofmt_xdate() draws the labels diagonally to prevent them from overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()