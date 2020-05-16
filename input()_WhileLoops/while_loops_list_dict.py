#To modify a list as you work through it, use a while loop.
#Don't use for loops if you want to modify lists, Python will trouble keeping track of items correctly.

#MOVING ITEMS FROM ONE LIST TO ANOTHER:
unconfirmed_users = ["drudzi", "frozty", "kaw", "hamlet_j", "bumba", "gandai"]
confirmed_users = []

while unconfirmed_users: #IMPORTANT: When only a list is given, it's considered True as long as it ISN'T EMPTY.
    user = unconfirmed_users.pop() #Grabs last user in list.
    
    print(f"Verifying user: {user.title()}")
    confirmed_users.append(user) #Adds user to last spot in another list.

print("\nThe following users have been confirmed:")
for user in sorted(confirmed_users):
    print(user.title())
print()


#REMOVING ALL INSTANCES OF SPECIFIC VALUES FROM A LIST:
#Want to remove all 'cat' strings from a big list of lots of animals?
animals = ['dog', 'cat', 'pig', 'cat', 'cow', 'dog', 'cat', 'cat', 'bird', 'horse', 'pig', 'horse']
print(animals)

while 'cat' in animals: #As long as it finds any 'cat' value in list, it's TRUE.
    animals.remove('cat')
#Stops when there are no more 'cat'.
print(animals)


#FILLING A DICTIONARY WITH USER INPUT():
responses = {} #Setting up a dict.
active = True #Setting a flag to indicate that loop is still active.

while active:
    name = input("\nWhat's your name? ")
    response = input("Who is your favorite football player? ")

    responses[name] = response #Storing the response together with name(key) in dict.

    repeat = input("Would you like to let another person respond? (yes/no) ")
    #Asking if any other person wants to continue. Otherwise quit looping.
    if repeat == 'no':
        active = False

print("These are the polling results:")
for name, response in responses.items():
    print(f"{name.title()}'s favorite player is {response.title()}.")