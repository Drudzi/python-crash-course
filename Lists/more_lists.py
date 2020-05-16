players = ["charlie", "erik", "florence", "martina", "john", "kawan", "drudzi", "frozty", "hamlet_j"]

print(players[1:4]) #This is called slicing. First index tells where to start counting, and last index tells where to end.
                    #1:4 prints item 2-4 (index 1-3)

print(players[4:]) #When only first index is given, it starts there and goes all the way til the end of list.

print(players[:5]) #When only second index is given, it starts from index 0 til given index.

print(players[-4:]) #Negative numbers start from the end and goes navigates left in the list, with last index in list being -1.
                    #This starts at 4th from the right and goes til end of list.

print(players[:-4]) #This functions the same, but instead it starts at index 0 and goes no further than index: -4. Leaves out the last four items.

print(players[::2]) #A third given number decides step length between every item it should print. With a 2, it prints every second item.

#Looping through a slice:
for player in players[-4:]: #Last 4 players in team.
    print(player.title())

print()

for player in players[:3]: #First three players in team.
    print(player.title())

print()

#Copying lists:
team = players[:]   #Copies list of players into a new list called "team". 
                    #Without any given numbers inside the square brackets, it takes the whole list.
#team = players won't work if you want "team" and "players" to be separate lists. It associates both variables with the same original list.

team.append("gandai")
print(players)
print(team)