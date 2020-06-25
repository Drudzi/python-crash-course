from operator import itemgetter

import requests

# Make an API call and store the response:
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")
#This API contains a list of the IDs to the 500 most popular articles on Hacker News.

# Process information about each submission:
submission_ids = r.json() #We convert and store the repsonse list in submission_ids.
submission_dicts = []
#We'll use these IDs to build a set of dictionaries that each store info about the current submission.
# We'll store these dictionaries in the empty list called submission_dicts.

for submission_id in submission_ids[:30]: #We loop through the IDs of the top 30 submissions.
    # Make a separate API call for each subbmission:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    #We make a new API call to get more info about the current article in the loop.
    # This API returns a dictionary json, so we convert it to a Python dict and store it.

    # Build a dictionary for each article:
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    #We create a custom dictionaries to store valueable information from the article.
    # We reach the information using the response_dict we just created.
    
    submission_dicts.append(submission_dict)
    #We append the current article's dictionary to our list.

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
#Here, we want to sort our list of dictionaries. In this case we want to sort by amount of comments.
# The itemgetter() function from the operator module lets us sort by a key in a dictionary.
#  We know that all of the dictionaries in the list has the same structure...
#   so each dictionary should have a comment key.
#    We pass itemgetter the 'comment' key and it will make our sorted() function...
#     use these values as its basis for sorting the list.
#      In order to place the most-commented articles first, we reverse it.

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
    #We loop through the dicts and print some cool information.