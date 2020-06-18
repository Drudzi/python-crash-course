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

# Map the fires:
data = [{
    'type': "scattergeo",
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': 2,
        'color': brights,
        'colorscale': "Inferno",
        'colorbar': {'title': "Brightness"},
    }
}]

layout = Layout(title="Global Fires, last 7 days")

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='global_fires.html')