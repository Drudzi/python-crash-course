import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'world_fires_7_day.csv'
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
    'lat': lats,
    'lon': lons,
    'marker': {
        'size': [5*bright in brights],
        'color': brights,
        'colorscale': "Inferno"
        'colorbar': {'title': "Brightness"}
    }
}]