#   STORING DATA:

#A lot of times, you'll ask for user input data.
#Whatever program you're writing, you'll store that information...
# in data structures such as lists and dictionaries.

#When users close a program, you'll probably want to save the information they entered.
#A simple way to do this is to use the 'json' module.

#The json module lets you dump data structures into files...
# and then load that data the next time the program runs.

#json can also be used to share data between different Python programs.
#Not only to Python programs actually...
# the JSON data format isn't specific to Python, you can share it with many other programming languages.

#   JSON (JavaScript Object Notation) originally developed for JavaScript, is now used i many languages. 


#   Using json.dump() and json.load():

import json #importing the json module.

#Let's store a list of numbers in a file using json.dump():
numbers_1 = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json' #we format file to .json, it's the most common way to indicate it's a json file.
with open(filename, 'w') as f: #opening with write mode, which allows json to write to it.
    json.dump(numbers_1, f) #We use json.dump() to store the list of numbers in numbers.json.
                            #json.dump() takes two arguments, 1(a piece of data) and 2(a file to store in).

#Let's use json.load() to read the list back into memory:
filename = 'numbers.json'
with open(filename) as f: #We open the file we just used to dump some numbers into. Opening in default 'r'.
    numbers_2 = json.load(f)
    #We use json.load() which needs a file object in arguments to get data from. It loads data into numbers_2.

print(numbers_2) #Checking it's the same list as numbers_1.
print(numbers_1)


#   Saving and reading user-generated data:
#You most likely want to store user-generated data to not lose it.
#json is useful for this:

#Example: First time running, we prompt the user for his name, but when he logs on again it's remembered.

filename = 'username.json'
try:
    with open (filename) as f:
        username = json.load(f) #We try if the file already exists and has a username. Then go to else-block.
        # if json finds the file empty here, it will return error because it can't load anything.
except FileNotFoundError:
    username = input("What is your name? ") #If file not found we prompt for username.
    with open(filename,'w') as f:
        json.dump(username, f) #We store that username in json file, so we can open it next time!
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!") #If username is found, we remember it and print hello!


#   Refactoring:

#You will often see possible improvements in your code that actually already works.
#Often, you'll recognize that you can break up your code into different specific functions.
#Dividing code into more specific functions will often increase readability of code!

#Splitting up code into specific funtctions is called REFACTORING.

#Let's refactor the "remember user" code above:

def get_stored_username():
    """Get stored username if available.""" #Don't forget docstring.
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Get new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Hello, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you, {username}!")

greet_user()

#Now each function in this version has a single, clear purpose.
#We can now do everything using just one function call!

#This compartmentalization of work is an essential part of writing clear code easy to maintain and extend.
#     to compartmentalize means to separate something into isolated parts.



# 10-13. Verify user:

