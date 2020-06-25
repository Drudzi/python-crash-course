import plotly.graph_objects as go
from plotly import offline
import numpy as np

from random_walk import RandomWalk

rw = RandomWalk(10_000)
rw.fill_walk()

steps = go.Scatter(x=rw.x_values, y=rw.y_values, mode='markers', 
    marker=dict(size=4, color=list(range(rw.num_points)), colorscale='Inferno_r', showscale=True),
    name='Random Walk')
my_layout = go.Layout(title='Random Walk of 10.000 points')

offline.plot({'data': steps, 'layout': my_layout}, filename='random_walk.html')