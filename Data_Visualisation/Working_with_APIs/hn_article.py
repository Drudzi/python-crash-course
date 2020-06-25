import requests
import json

# Make an API call and store the response:
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url) #This is our call to the API.
print(f"Status code: {r.status_code}") #IF status code 200, it is working correctly.

# Explore the structure of the data:
response_dict = r.json() #Collecting the API data and storing it as a Python dict.
readable_file = 'readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)