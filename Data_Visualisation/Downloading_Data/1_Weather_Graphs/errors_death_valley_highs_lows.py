#In this program, we handle missing data by using try-except-else...
# but sometimes you can also use continue to skip data or use remove or del to eliminate data.
#  Use any approach that works as long as the result is a meaningful and accuracte visualization.

from datetime import datetime
import csv

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file:
    dates, highs, lows = [], [], []
    for row in reader:        
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
            #Tries to find temp data.
        except ValueError:
            #If not and a ValueError occur, it skips the else block and print the following.
            print(f"Missing data for {current_date}")
        else:
            #If try was successful, it appends values to appropriate lists.
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            #Now, we have the max temps, low temps and the dates stored!

# Plot the high temperatures:
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.9)
ax.plot(dates, lows, c='blue', alpha=0.9)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot:
plt.title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() #autofmt_xdate() draws the labels diagonally to prevent them from overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()