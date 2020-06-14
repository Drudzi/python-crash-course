import csv
# The csv module is from the Python standard library and helps working with and reading csv files.

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) #We assign a csv.reader object to reader, which reads the csv.
    header_row = next(reader)
    #The next() function returns the next line in the csv when a reader object is passed.
    #We only call it once, which gives is the headers which contain meaningful information about the data.
    #The reader object takes all csv's in the first line and stores them in a list.

    for index, column_header in enumerate(header_row):
        print(index, column_header)
        #enumerate() returns both the index and the value of each item when looping through a list.
    