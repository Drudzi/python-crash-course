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
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts: #Collecting data from the API.
    repo_name = repo_dict['name'] #The name of the actual project.
    repo_url = repo_dict['html_url'] #URL for project on GitHub.
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    #Plotly let's us use HTML code, which let's us add links to our chart.
    # We use the HTML anchor tag to generate the link, an anchor tag looks like this:
    #  <a href='URL'>link text</a>
    #   In other words, the anchor tag let's you make a link where you cover the URL with a custom text.
    #We assign the current URL and "cover" it with the name of the current project.

    repo_links.append(repo_link)

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
    'x': repo_links, #We assign the project-links to the x-values, so you easily can click their links.
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