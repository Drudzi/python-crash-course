#Looping through all Key-Value pairs:
user_0 = {
    'username': "efermi",
    'first': "enrico",
    'last': "fermi"
    }
print(user_0.items()) #Items method returns a list of key-value pairs inside dictionary.

for key, value in user_0.items(): #Key, value could be anything like 'k, v'. They are two variables that hold the key and the value in each pair.
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jonathan': "python",
    'johan': "c",
    'koffe': "java",
    'carl': "c#",
    'hasse': "ruby",
    'justin': "pascal",
    'göran': "python",
    'malte': "javascript",
    'bill': "python",
    'kawan': "java",
    }

print()
for name, language in favorite_languages.items(): #name var. holds every key and language var. holds every associated value.
    print(f"{name.title()}'s favorite language is {language.title()}!") #Using variables like name and language makes it more readable and clear.
print()

print(favorite_languages.keys()) #Similar to items() method, instead brings a list of all keys only.
#Useful when only keys are needed, maybe when you want to see who took a poll:
print()

for name in favorite_languages.keys():
    print(f"Thanks for taking the poll, {name.title()}!")
print()
#Looping through the keys is actually default behaviour when going through a dictionary.
for name in favorite_languages: #This loop will return same output.
    print(f"Thanks for taking the poll, {name.title()}!")
print()
#keys() method can be used for readability.

friends = ["hasse", "koffe"] #List of friends we want to print a message to.
for name in favorite_languages.keys():
    print(f"Hi {name.title()}!") #We say hello to everyone!
    if name in friends: #We check whether the name is one of our friends.
        language = favorite_languages[name].title() #If it is, we give var. language their favorite language.
        print(f"\t{name.title()}, I see that you love {language}.") #Then, we print a special message including their favorite language.
print()

if 'erik' not in favorite_languages.keys(): #Keys() method can also be used to look for keys in if-statements. 
    print("Erik, please take our poll!")
print()

for name in sorted(favorite_languages.keys()): #If you want the keys ordered in alphabetics, sorted() temporarily does that.
    print(f"{name.title()}, thank you for taking the poll!")
print()

#Looping through all VALUES in a dictionary:
#values() method returns a list of values without any keys.
print("The following languages have been mentioned:")
for language in favorite_languages.values(): #Prints every value, also duplicates.
    print(language.title())
print()

#If we don't want any duplicates and only unique values, we use set() method.
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): #Set() method identifies unique items in list and builds a set from those items.
    print(language.title())
print()

#You can build sets directly using braces and separating elements with commas.
my_set = {'braces', 'brackets', 'parentheses'}
#Sets look very similar to dictionaries as you can see, both are wrapped in braces {}.
#Braces that doesn't include key-value pairs are most likely sets.
#Unlike lists and dictionaries, sets don't keep items in any specific order.


# 6-5. Rivers:

#Loop printing a sentence about each river, using both key and value.
rivers = {'nile': "egypt", 'amazonas': "brazil", 'yangtze': "china", 'volga': "russia", 'donau': "europe"}
for river, country in rivers.items(): #Items is required in order to recieve both key and associated value.
    #Without items() it only recieves keys and should only be asking for one value using only one variable.
    print(f"The {river.title()} river runs through {country.title()}.")
print()

#Loop printing the name of each river.
print("The following rivers are in the dictionary:")
for river in rivers.keys(): #keys() method isn't required, but improves readability.
    print(river.title())
print()

#Loop printing name of each country:
print("The following countries are in the dictionary:")
for country in rivers.values():
    print(country.title())
print()


# 6-6. Polling:
favorite_languages = {
    'jonathan': "python",
    'johan': "c",
    'koffe': "java",
    'carl': "c#",
    'hasse': "ruby",
    'justin': "pascal",
    'göran': "python",
    'malte': "javascript",
    'bill': "python",
    'kawan': "java",
    }
should_poll = ['koffe', 'melinda', 'jeff', 'kawan']

for name in should_poll:
    if name in favorite_languages.keys():
        print(f"Thanks for taking the poll {name.title()}!")
    else:
        print(f"Feel free to take our poll {name.title()}!")