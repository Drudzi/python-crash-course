from plotly.graph_objs import Bar
from plotly import offline

from hn_submissions import submission_dicts

# Collect data:
comments, submission_links = [], []
for i in submission_dicts:
    comments.append(i['comments'])

    submission_title = i['title']
    submission_url = i['hn_link']
    submission_link = f"<a href='{submission_url}'>{submission_title}</a>"
    submission_links.append(submission_link)

# Visualize data:
data = [{
    'type': 'bar',
    'x': submission_links,
    'y': comments,
}]
layout = {
    'title': "Most Commented Articles on Hacker News",
    'titlefont': {'size': 20},
    'xaxis': {
        'title': "Article",
        'titlefont': {'size': 20},
        'tickfont': {'size': 10},
    },
    'yaxis': {
        'title': "Comments",
        'titlefont': {'size': 20},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='most_commented_articles.html')