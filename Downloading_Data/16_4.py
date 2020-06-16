# AUTOMATIC INDEXES

from datetime import datetime
import csv

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(reader)

    # Get dates, station name, and high and low temperatures from this file:
    dates, highs, lows = [], [], []
    tmax = header_row.index('TMAX')
    tmin = header_row.index('TMIN')

    for index, row in enumerate(reader):        
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        if index == 1:
            station_name = row[1].upper()
        try:
            high = int(row[tmax])
            low = int(row[tmin])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
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
plt.title(f"Daily high and low temperatures - 2018\n{station_name}", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.ylim(20, 140)

plt.show()