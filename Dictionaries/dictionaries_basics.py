#               ---> ESSENTIALS <---
#A dictionary in Python is a collection of key-value pairs.
#Each key is connected to a value.
#Any object or data type can be used as a value in a dictionary.

alien_0 = {'color': "green", 'points': 5} #Dictionary is wrapped in braces.
#Key-value pair is set of associated values.
#When key is provided, it returns associated value.
#Every key is connected to its value by a colon.
#Each key-value pair is separated by commas.
#A dictionary can store unlimited key-value pairs.

print(alien_0["color"]) #Value can be reached using the associated key, this will return green.
print()

alien_0 = {'color': "green", 'points': 5}

new_points =+ alien_0['points'] #If alien_0 is shot down, you get 5 new points. 
#new_points =+ value is easier way of adding a value to a variable instead of new_points = new_points + value
print(f"You just earned {new_points} points!\n")

#Adding new key-value pairs:
print(alien_0) #Original dictionary.

alien_0['x_position'] = 0 #Adding key-value pairs.
alien_0['y_position'] = 25 #Value of key is defined in square-brackets and value right of equal sign defines its associated value.

print(alien_0) #With its new pairs.

alien_1 = {} #You can also start with an empty dictionary.
alien_1['color'] = "red"
alien_1['points'] = 20
print(f"\nThis is alien 1:\n{alien_1}\n")

#Modifying values:
print(alien_1['color'])

alien_1['color'] = "blue" #Modifying color value.
print(alien_1['color'])

#Giving some new values.
alien_1['x_position'] = 0
alien_1['y_position'] = 25
alien_1['speed'] = "medium"
print(f"Original x-position: {alien_1['x_position']}")

#Move alien_1 to the right.
#Determine how far to move alien based on current 'speed'.
if alien_1['speed'] == "slow":
    x_increment = 1
elif alien_1['speed'] == "medium":
    x_increment = 2
else:
    #This must be a "fast" alien.
    x_increment = 3

#New postition is old position plus x_increment:
alien_1['x_position'] =+ x_increment
print(f"New position: {alien_1['x_position']}")

print()

#Deleting key-value pairs:

print(alien_1)
del alien_1['points'] #del command removes given key-value pair permanently.
print(alien_1)

#A dictionary of similar objects:
favorite_languages = {
    'jonathan': "python",
    'johan': "c",
    'koffe': "java",
    'carl': "c#",
    'hasse': "ruby",
    'justin': "pascal"
    }

language = favorite_languages['jonathan'].title()
print(f"\nJonathan's favorite language is {language}.\n")

#If a key doesn't exist:
#print(favorite_languages['eric']) #This returns error because it can't find 'eric' in dictionary.

#Using get() to access values:
print(favorite_languages.get('eric', 'Sorry, Eric has not entered his favorite language'))
print(favorite_languages.get('jonathan'))
#Get function above needs at least one argument.
#First argument should be a key.
#Second argument should be a default value to return if key in 1st argument doesn't exist.
#get() is good method when the key you are asking for might not exist.
print(favorite_languages.get('eric')) #If given key, doesn't exist and there is no second argument given:
#Python will return the value 'None'. Not an error.
print()

# 6-2. Favorite numbers:
favorite_numbers = {
    'jona': 8,
    'schweini': 31,
    'isak': 24
    }
for name in favorite_numbers.keys():
    number = favorite_numbers[name]
    print(f"{name.title()}'s favorite number is {number}.")