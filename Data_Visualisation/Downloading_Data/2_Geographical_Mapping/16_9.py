import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    lats, lons, brights, hover_texts = [], [], [], []
    for row in reader:
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        brights.append(float(row[2]))
    
for brightness in brights:
    text = f"Brightness: {brightness}"
    hover_texts.append(text)

# Map the fires:
data = [{
    'type': "scattergeo",
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [0.03*brightness for brightness in brights],
        'color': brights,
        'colorscale': "Inferno",
        'reversescale': True,
        'colorbar': {'title': "Brightness"},
    }
}]

layout = Layout(title="Global Fires, last 24 hours")

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='global_fires.html')