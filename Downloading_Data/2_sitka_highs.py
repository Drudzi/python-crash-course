import csv
# The csv module is from the Python standard library and helps working with and reading csv files.

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) #We assign a csv.reader object to reader, which reads the csv.
    header_row = next(reader)
    #The next() function returns the next line in the csv when a reader object is passed.
    #We only call it once, which gives is the headers which contain meaningful information about the data.
    #The reader object takes all csv's in a line and stores them in a list.

    # Get high temperatures from this file:
    highs = []
    for row in reader:
        #Looping through all the remaining rows of the csv file associated with the reader object.
        # It continues from where it left off, meaning it won't include the header in the highs list.
        #  row will always be a list of values from the csv file.
        high = int(row[5]) #Pulling the 5th value (max temp) from the row and converting it from str to numerical (integer).
        highs.append(high)
        #Now, we have the max temps stored in the highs-list!
    
    print(highs)