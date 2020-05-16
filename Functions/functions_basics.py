#DEFINING A FUNCTION:

def greet_user_0():
    """Display a simple greeting.""" #This is a docstring, they are enclosed in triple quotes. Generates documentation for function.
    #Docstrings should describe what a function does.
    print("Hello!")
greet_user_0()


#PASSING INFORMATION TO A FUNCTION:
def greet_user_1(username): #When defining function, enter a variable name inside parentheses.
    #When calling function, write some value in parentheses and it is assoctiated with variable(username) in function.
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user_1('drudzi')


#ARGUMENTS AND PARAMETERS:

#In definition-line of function greet_user_1, the variable username is an example of a parameter.
#A parameter is a piece of information the function needs to do its job.

#The value 'drudzi' in the function-call, is an example of an argument.
#An argument is a piece of information that's passed from a function call to a function.

#Argument 'drudzi' was passed to the function greet_user_1(), and value was assigned to the parameter username.

#If you give define a function with some parameters, it won't run without given arguments for all parameters.



#PASSING ARGUMENTS:


# Positional arguments:
#These arguments are assigned to the parameter with the same index.
#The order of arguments should match order of parameters.
def describe_pet(animal_type, pet_name): #1st parameter wants animal type and 2nd wants pet's name.
    #Make sure to match this order when giving the arguments.
    """Display information about a pet"""
    print(f"\nI have a {animal_type.lower()}.")
    print(f"My {animal_type.lower()}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') #1st argument should match the type of animal and 2nd should match pet's name.

#Order matters in positional arguments:
describe_pet('harry', 'hamster') #This is wrong order. 
#Returns "My harry's name is Hamster."


# Keyword arguments:
#A keyword argument is a key-value pair you pass to a function.
#If parameter is pet_name, you write pet_name = 'harry' as the argument.
#This way, Python sees which parameter you want to assign a value to.
#You no longer need to order them correctly.

#These function calls will give the exact same result:
describe_pet(animal_type='dog', pet_name='zlatan')
describe_pet(pet_name='zlatan', animal_type='dog')
#They are not in same order, but that doesn't matter when using keyword arguments!


# Default values:
#When defining a function, you can always assign a default value to a parameter.
#If an argument is provided for a parameter, it uses the argument value.
#If no argument is provided, it uses the parameter's default value.
#You have to manually set a default value and when you have, you don't need to give the parameter an argument for the function to run.

# EXAMPLE: If you notice most calls use argument 'sweden' for parameter country, you can set 'sweden' as default.
def your_country(name, country='sweden'):
    """Display given name and their country."""
    print(f"\nMy name is {name.title()} and I am from {country.title()}.")

your_country(name='jonathan') #Parameter country don't need argument because it has a default. Assumes I'm from Sweden.
your_country('jonathan') #Returns same as above.
#When only 'jonathan' is given, Python sees it as a postitional argument and gives it to first parameter name.
#List parameters with default values last.

your_country('jonathan', 'norway')
your_country(name='jonathan', country='norway')
your_country('jonathan', country='norway')
#All methods above can be used to give another value than default to parameter country.
print()


# Equivalent function calls:
def describe_animal(age, animal_type='dog'):
    """Display information about an animal."""
    print(f"The {animal_type.lower()} is {age} years old.")

#Consider definition above.
#There are several ways of getting the sam result.

#A dog aged 10:
describe_animal(10)
describe_animal(age=10) #If the animal is a dog, you don't need to give animal_type.
print()

#A hamster aged 5:
describe_animal(5, 'hamster')
describe_animal(age=5, animal_type='hamster')
describe_animal(animal_type='hamster', age=5)


#AVOIDING ARGUMENT ERRORS:
#Unmatched arguments is a common type of error.
#They occur when you provide fewer or more arguments than a function needs to do its work.

#describe_animal()...will give error.

#Python is helpful and tells you what kind of arguments to provide in the traceback.
print()



#RETURN VALUES:
#Functions does not need to print its output.
#They can also process any data type and return a value or a set of values.
#The value returned is called a RETURN VALUE.

#Returning a simple value:
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title() #THIS IS THE RETURN COMMAND. Given value is the return value.

musician = get_formatted_name('jimi', 'hendrix') #When calling a function that returns a value, you need to assign it to a variable.
print(musician)


#Making an argument optional:
#We rebuild get_formatted_name to also include middle name, but for middle name to be optional.

def get_formatted_name_1(first_name, last_name, middle_name=''): #Notice that middle name is last. Optional parameters should always be last.
    """Return a full name, neatly formatted."""
    #middle_name default is an empty string.
    #Python interprets non-empty strings as True:
    if middle_name: #If middle_name isn't empty (has been given a value), do the following.
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

print(get_formatted_name_1('jonathan', 'axelsson'))
print(get_formatted_name_1('jonathan', 'axelsson', 'reine')) #Using positional arguments.


#Returning a dictionary:
#Function can return any data type, including more complicated data structures like lists and dictionaries.
def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name} #Building a dictionary of name.
    return person

person = build_person('jonathan', 'axelsson') #Jonathan is now labeled a first name and Axelsson is labeled a last name.
#This function takes in simple data and puts it into a meaningful data structure that can do more than just printing it.
print(person) #Prints the dictionary.

#Extending build_person to accept some optional values that will get stored in the dictionary about the person:
def build_person_1(first_name, last_name, middle_name='', age=None): #None is like ''(empty string), but for numbers. 
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name} #Building a dictionary of name.
    if middle_name:
        person['middle'] = middle_name
    if age: #If age != None, do the following.
        person['age'] = age
    return person


#Using a function with a while loop:
def get_formatted_name_2(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("Please tell me your name:")
    print('Enter "quit" to exit.')
    first = input("First name: ")
    if first.lower() == 'quit':
       break #If user don't want to continue, break out of loop.
    last = input("Last name: ")
    if last.lower() == 'quit':
        break

    formatted_name = get_formatted_name_2(first, last)
    print(f"Hello, {formatted_name}!")