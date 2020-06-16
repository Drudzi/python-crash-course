import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfall_data = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        try:
            rainfall = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rainfall_data.append(rainfall)
    
# Visualize data:
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfall_data)

#   Style plot:
plt.title('Rainfall in Sitka - 2018', fontsize=20)
plt.xlabel('')
fig.autofmt_xdate()
plt.ylabel('Amount (m)')
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()