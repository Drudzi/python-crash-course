#Nesting is when you store dictionaries in a list or a list inside a dictionary, or even a dictionary inside a dictionary.

#DICTIONARIES IN LISTS:
alien_0 = {'color': "green", 'points': "5"}
alien_1 = {'color': "yellow", 'points': "10"}
alien_2 = {'color': "red", 'points': "15"}

aliens = [alien_0, alien_1, alien_2] #Storing multiple alien-directories in a list.
for alien in aliens:
    print(alien)

#Making a fleet of 30 aliens:
aliens = [] #Empty list for storing aliens.

for number in range(30):
    new_alien = {'color': "green", 'points': "5", 'speed': "slow"} #Makes a new alien every number.
    aliens.append(new_alien) #Adds it to aliens-list.
#aliens-list now contains 30 new_aliens.

for alien in aliens[:5]: #Shows first five aliens in our fleet.
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}") #Showing amount of items inside aliens-list. Confirms 30 aliens have been created.

#All 30 aliens have same characteristics, but because every alien is considered a separate object, we can modify them.
#Changing first three aliens:
for alien in aliens[:3]:
    if alien['color'] == "green":
        alien['color'] = "yellow"
        alien['points'] = '10'
        alien['speed'] = "medium"

for alien in aliens[:5]: #Shows first five aliens in our fleet to check if first three has been modified.
    print(alien)

#It's common to store dicionaries in lists when each dictionary contains information about one type of object.
#ex) You might store information about users in separate dictionaries and store those dictionaries in a list called users.



#A LIST IN A DICTIONARY:
#ex) Useful when describing a ordered pizza.
        #A list can only carry one aspect, such as toppings.
        #With a dictionary you can use unlimited amount of aspects.

#Below, two kinds of information are stored about a pizza in a dictionary:
pizza = {
    'crust': "thick",
    'toppings': ["mushrooms", "extra cheese", "pepperoni"],
    }

#Summarize the order:
print(f"You ordered a {pizza['crust']}-crust pizza " #If print call will get too long, do the following, remember to intend after break.
    "with the following toppings:")
for topping in pizza['toppings']: #pizza['toppings'] is read like any other list.
    print(f"\t{topping.capitalize()}")
print()

favorite_languages = {
    'jonathan': "python",
    'johan': "c",
    'koffe': "java",
    'carl': "c#",
    'hasse': ["ruby", "c++", "java"], #Value associated with Hasse is a list of three languages.
    'justin': "pascal",
    'göran': ["python", "pascal"],
    'malte': "javascript",
    'bill': ["python", "basic"],
    'kawan': "java",
    }

for name, languages in favorite_languages.items(): #items() gives access both key and value. Without it would only reach the keys.
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}") #When iterating a name with only one language as a value which is not in a list,
                                        #it sees every unique letter as an object. See output.
                                        #You need to make sure every value is a list in order to get a similar output for every name.

favorite_languages = { #Making all values to lists.
    'jonathan': ["python"],
    'johan': ["c"],
    'koffe': ["java"],
    'carl': ["c#"],
    'hasse': ["ruby", "c++", "java"],
    'justin': ["pascal"],
    'göran': ["python", "pascal"],
    'malte': ["javascript"],
    'bill': ["python", "basic"],
    'kawan': ["java"],
    } 

for name, languages in favorite_languages.items(): #items() gives access both key and value. Without it would only reach the keys.
    if len(languages) == 1:
        print(f"{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
print() #Now it works perfect, because all values are lists.



#A DICTIONARY INSIDE A DICTIONARY:
users = {
    'aeinstein': {
        'first': "albert",
        'last': "einstein",
        'location': "princeton"
        },
    'mcurie': {
        'first': "marie",
        'last': "curie",
        'location': "paris"
        },
    }
print(users.items())
print()
#We create a dictionary with two keys, one for every user.
#Every key's value is a dictionary with keys containing their first name, last name and location.

for username, user_info in users.items(): #We loop through the 'users' dictionary.
    #Each key is assigned to first given variable 'username'.
    #Each value (in this case each dictionary) is assigned to variable user_info.
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}" #We begin accessing inner dictionary, user_info contains dictionary of
                                                            #user information of current user.
    location = user_info['location'] #Note that structure of each key's (user's) dictionary is identical.
                                        #Makes it easier to work with. Otherwise code inside for loop would be way more complicated.

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
print()


# 6-8. Pets:
animal_0 = {'name': "elsa", 'animal': "cat", 'age': 8, 'owner': "cajsa"}
animal_1 = {'name': "rosa", 'animal': "cat", 'age': 2, 'owner': "jonathan"}
animal_2 = {'name': "molly", 'animal': "dog", 'age': 8, 'owner': "andreas"}
pets = [animal_0, animal_1, animal_2]

print("These are my pets:")
pet_count = 0
for pet in pets:
    print()
    pet_count += 1
    if pet_count == 1:
        print("This is my first pet:")
    elif pet_count == 2:
        print("This is my second pet:")
    elif pet_count == 3:
        print("This is my third pet:")
    print(f"\tName: {pet['name'].title()}")
    print(f"\tAnimal: {pet['animal'].title()}")
    print(f"\tAge: {pet['age']}")
    print(f"\tOwner: {pet['owner'].title()}")


# 6-9. Favorite Places:
favorite_places = {'erik': ["djursvik", "tokyo"], 'kawan': ["söderåkra centrum", "kurdistan", "turkiet"], 'isak': ["böke", "spanien"]}
for name, places in favorite_places.items():
    if len(places) == 2:
        places_print = f"{places[0].title()} och {places[1].title()}"
    elif len(places) == 3:
        places_print = f"{places[0].title()}, {places[1].title()} och {places[2].title()}"
    print(f"\nHej, jag heter {name.title()}.\nMina favoritplatser är {places_print}!")