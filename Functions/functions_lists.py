#PASSING A LIST TO A FUNCTION:
#When a list is passed to a function, it gets direct access to items in list.

#We have a list of users and want to print a greeting to each:
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names: #Loops through given list. 
        message = f"Hello, {name.title()}!"
        print(message)

usernames = ['drudzi', 'hamlet', 'gandai', 'frozty', 'bumba', 'kakan', 'footballscrazy']
greet_users(usernames)
print()


#MODIFYING A LIST IN A FUNCTION:
#When a list is passed to a function, the function can also modify it.
#Any change to a list inside a function is permanent.

#Conisider a company that creates 3D printed models of designs that users submit:
#Without using a function:
unprinted_designs = ['phone case', 'robot toy', 'star wars soldier'] #Some submitted designs that needs to be printed.
completed_models = []
while unprinted_designs: #while unprinted_designs is not empty...
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for model in completed_models:
    print(model)
print()

#The code above can be more carefully structured and organized using functions:
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Display all the models that were printed."""
    print(f"\nThe following models have been printed:")
    for model in completed_models:
        print(model)

unprinted_designs = ['phone case', 'robot toy', 'star wars soldier'] #Some submitted designs that needs to be printed.
completed_models = []

print_models(unprinted_designs, completed_models) #Giving lists above as arguments.
show_completed_models(completed_models)

#If same code will be used several time it's much easier to extend or maintain using functions.
#Every function should have one specific job, making it easy to read and work with.
#It's better, more beneficial and easier to have several job-specific functions rather than one big who does it all.


#PREVENTING A FUNCTION FROM MODIFYING A LIST:
#Consider the list unprinted_designs in section above.
#Maybe you want to keep the original version of it, without emptying it.
#For that case, you can pass the function a copy of it instead:
#   function_name(list_name[:])    This is how you pass a copy of a list.
#Slice notation [:] makes a copy of the list to send to the function.

print_models(unprinted_designs[:], completed_models)
#Original unprinted_designs will not be affected by function call above.

#It's most of the time, better to pass an original list to a function unless you have a specific reason.
#Passing original lists avoid using the time and memory needed to make separate copies, especially when working with large lists.



#PASSING AN ARBITRARY NUMBER OF ARGUMENTS:
#Sometimes you don't know how many arguments a function needs.
#Python has a method to collect an arbitrary amount of arguments.

#Consider a function that builds a pizza and accepts any number of toppings:
def make_pizza(*toppings): # Asterisk tells Python to make a tuple called 'toppings', and store whatever values it recieves into this tuple.
    """Print the list of toppings that have been requested."""
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print('-',topping)

make_pizza('kebab')
make_pizza('kebab', 'salami', 'pepperoni')


#Mixing positional and arbitrary arguments:
#If you want a function to accept several types of arguments, the *(arbitrary) parameter should always be last.
#Python matches positional- and keyword arguments first, and then collects remaining arguments in *-parameter.

#Consider make_pizza() to also take in a size:
def make_pizza_1(size, *toppings): #We put *toppings last.
    """Summarize the pizza we're about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print('-',topping)

make_pizza_1(12, 'kebab', 'salami', 'pepperoni')


#Using arbitrary keyword arguments:
#Sometimes you want to accept an arbitrary number of arguments, but you don't know what kind of information.
#Then, you can write functions that accept any amount of key-value pairs.

def build_profile(first, last, **user_info): #Double asterikses ** creates a dictionary called user_info.
    #This dictionary can recieve any amount of key-value pairs when function is called.
    """Build a dictionary containing everything we know about a user."""
    user_info['first name'] = first #Adding required first name to user_info dictionary.
    user_info['last name'] = last   #Adding required last name to user_info dictionary.
    return user_info #Returns the dictionary.

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics') #Entering required name parts and...
                                                                                          #key-value pairs 'location' and 'physics'.

print(user_profile)


# 8-12. Sandwiches:
def sandwich(*items):
    """Build a sandwich."""
    if len(items) == 1:
        print(f"\nMaking your sandwich, with {len(items)} item on.")
    else:
        print(f"\nMaking your sandwich, with {len(items)} items on.")
    print("Your sandwich is ready, it contains:")
    for item in items:
        print("-", item)

sandwich('ham', 'cheese', 'pepper')
sandwich('salad', 'chicken')
sandwich('cucumber')


# 8-14. Cars:
def make_car(manufacturer, model, **car):
    """Store given information about a car in a dictionary."""
    car['manufacturer'] = manufacturer
    car['model'] = model
    return car

print(make_car('tesla', 'cybertruck', engine='trimotor', horsepowers=850))