import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response:
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results:
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts: #Collecting data from the API.
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login'] #Name of the owner.
    description = repo_dict['description'] #Description of the project.
    label = f"{owner}<br />{description}"
    #We merge the owner and description together in a string and store it in a variable.
    #Plotly let's us use HTML code within text elements...
    # so we generate a line break using (<br />).

    labels.append(label)

# Make visualization:
data = [{
    'type': 'bar',
    'x': repo_names, #Names of the projects.
    'y': stars, #Amount of stars.
    'hovertext': labels, #Shows our labels strings when bars are hovered.
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
#We use the dictionary-way to make a chart object with our data.

layout = {
    'title': "Most-Starred Python Projects on GitHub",
    'titlefont': {'size': 24},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
#We also use the dictionary-way to make our layout.

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename="python_repos.html")