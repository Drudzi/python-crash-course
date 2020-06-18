from datetime import datetime
import csv
# The csv module is from the Python standard library and helps working with and reading csv files.
#  csv = comma-separated values

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) #We assign a csv.reader object to reader, which reads the csv.
    header_row = next(reader)
    #The next() function returns the next line in the csv when a reader object is passed.
    #We only call it once, which gives is the headers which contain meaningful information about the data.
    #The reader object takes all csv's in a line and stores them in a list.

    # Get dates and high temperatures from this file:
    dates, highs = [], []
    for row in reader:
        #Looping through all the remaining rows of the csv file associated with the reader object.
        # It continues from where it left off, meaning it won't include the header in the highs list.
        #  row will always be a list of values from the csv file.
        
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        #We use the datetime module and its strptime to convert the dates...
        # from string to an objects representing the dates.
        #  striptime() needs two arguments, the first one should be a string containing the date.
        #   The second argument should tell Python how the date is formatted.
        #    #See documentation or table 16-1.

        high = int(row[5]) #Pulling the 5th value (max temp) from the row and converting it from str to numerical (integer).
        dates.append(current_date)
        highs.append(high)
        #Now, we have the max temps and the dates stored!

# Plot the high temperatures:
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red') #Without any input values (x), it starts off at 0. Dates contains our input values.

# Format plot:
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() #autofmt_xdate() draws the labels diagonally to prevent them from overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()