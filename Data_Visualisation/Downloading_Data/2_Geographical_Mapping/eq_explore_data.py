import json
#We import the json module, which helps us handle json files.

# Explore the structure of the data:
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    #The json.load() function takes all data and converts it into a format Python can work with...
    # in this case it is a giant dictionary.

all_eq_dicts = all_eq_data['features'] 
#Length of this list should be 158 items, where every item is a dict about a single earthquake.

mags, lons, lats = [], [], []

for eq_dict in all_eq_dicts: #We loop through the list of dictionaries about the earthquakes.
    
    mag = eq_dict['properties']['mag']
    #The magnitude is stored in the nested 'properties' dictionary in the 'mag' key.
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    #Long- and latitudes are stored in nested 'geometry' dict in a list in the 'coordinates' key.
    
    mags.append(mag) #We store the magnitudes in the mags list.
    lons.append(lon)
    lats.append(lat)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    #We'll create a new file containing the same data but more readable. 
    json.dump(all_eq_data, f, indent=4)
    #json.dump() writes data to a json file, it takes a json file object and a file object to write to.
    # The indent parameter is what makes it more readable...
    #  it tell dump() to format the data using indentation that matches the data's structure.