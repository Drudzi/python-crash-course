import json

from plotly.graph_objs import Scattergeo, Layout #Scattergeo is the chart type we'll use.
from plotly import offline #We import offline to later render the map.

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
data_title = all_eq_data['metadata']['title']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:    
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title']) #The title contains a descriptive name of mag. and location.

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# Map the earthquakes:
data = [{
    'type': "scattergeo",
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    #The text key let's us assign labels to markers when hovered.
    # When we pass a list that matches the number of markers, Plotly gives individual labels for each marker.

    'marker': {
        'size': [6*mag for mag in mags],
        #The size key helps us specify the size of each marker.
        # We want the size to correspond to the magnitude of each earthquake.
        #  We could just pass it the mags list, but they would be too small if we did.
        #   That's why we use a for loop (LIST COMPREHENSION) to multiply each magnitude by 5.

        'color': mags, 
        #'color' tells Plotly what values it should use to determine where each marker falls on the colorscale.
        # We tell it too go after the magnitudes.

        'colorscale': "Inferno", #Determines which range of colors to use.
        'reversescale': True, #Reverses the colorscale if set to True.
        
        'colorbar': {'title': "Magnitude"},
        #Colorbar let's us configure the colorbar, we set a descriptive title.
    },
}]
#We make the Scattergeo chart object inside the data list.
# It can be done like this:
# data = [Scattergeo(lon=lons, lat=lats)] ... or like above in a dictionary which is easier to specify.
#  We use a list because you can plot more than one dataset in a visualization.
#   Scattergeo to scatter plot geographic data on a map.
#    The simplest uses of this chart only needs a list of longitudes and a list of latitudes.

my_layout = Layout(title=data_title)

fig = {'data': data, 'layout': my_layout} 
offline.plot(fig, filename='global_earthquakes.html')