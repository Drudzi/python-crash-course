import requests
#We import the requests module, which helps us request information from the web.

# Make an API call and store the response:
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#We store the url of the API call in the url variable.

headers = {'Accept': 'application/vnd.github.v3+json'}
#GitHub is currently on the third version of its API...
# so we define headers for the API call that ask explicitly to use this version.

r = requests.get(url, headers=headers)
#We use the request module and its get() function to make the call to the API.
 #We pass the get() our API url and then our HTTP header and store the response object in r.

print(f"Status code: {r.status_code}")
#The response object attribute called status_code which tells us whether or not the call was successful.
# A value of 200 means the call was successful.

# Store API response in a variable:
response_dict = r.json()
#The API returns the data in JSON format so we use the json() method to convert it to a Python dictionary.
print(f"Total repositories: {response_dict['total_count']}")
#Value associated with total_count returns total Python repositories on GitHub.

# Explore information about the repositories:
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}") #Checking how many repos we have data from.
#Value associated with 'items' is a list of dictionaries...
# each of which contains data about an individual Python repository.

# Examine the first repository:
repo_dict = repo_dicts[0] #We pull out the first dict to look closer at the data we've got.

print("\nSelected information about each repository:")
for repo_dict in repo_dicts: #With this loop we print some information about each repository.
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

# print(f"\nKeys: {len(repo_dict)}") #How many keys we have about each repo.
# for key in sorted(repo_dict.keys()):
#     print(key)
#     #We print what keys we have to see what kind of data there is.