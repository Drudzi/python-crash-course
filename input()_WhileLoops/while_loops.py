# The WHILE LOOP runs its given code as long as a condition is True.

current_number = 1
while current_number <= 5: #As long as current_number is less or equal to 5, run code below.
    print(current_number) #Will count to 5.
    current_number += 1

#Example use:
#A game should have an option allowing user to quit whenever they want.
#A while loop could say: run until user tells you to quit.

prompt = "\nTell me somethingm and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

message = "" #variable is given an empty string so the while loop has something to compare it too before any user input has come.
while message.lower() != 'quit': #Run as long as message isn't equal to 'quit'.
    message = input(prompt)
    if message.lower() != 'quit': #This line makes the program not to print quit when user gives that input, and quits it instantly.
        print(message)


#USING A FLAG:
#Complicated programs could have many events that could cause the loop to stop running.
# ex) In a game, multiple events should be able to stop the game, such as a player running out of boats or running out of time.

#You then might want ONE variable determining if the whole loop or program should be running.
#That variable is called a FLAG, acting as a signal to the program.
#We can write programs to run as long as flag = True and set it to stop when flag = False.

prompt = "\n[FLAG] Tell me somethingm and I will repeat it back to you."
prompt += "\nEnter 'quit' or 'game over' to end the program. "

active = True
while active: #As long as active variable is True, run program.
    message = input(prompt)

    if message.lower() == 'quit': #Stops program if given input is 'quit'.
        active = False #Sets our flag to false, which will stop the program.
    elif message.lower() == 'game over':
        active = False #Multiple tests can stop program with FLAG method.
    else:
        print(message)


#Using BREAK to exit a loop:
prompt = "\n[BREAK] Tell me somethingm and I will repeat it back to you."
prompt += "\nEnter 'quit' or 'game over' to end the program. "

while True: #A while True loop runs forever until a break statement is given.
    message = input(prompt)

    if message.lower() == 'quit' or 'game over':
        break #Break statement stops the loop instantly when it's reached. Good way to control which code is executed and when.
    else:
        print(message)


#Using CONTINUE in a loop:
#continue statement lets you return to the beginning of the loop, based on the result of a conditional test.

#Loop counting from 1-10, but only printing odd numbers:
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue #If current_number is even, continue statement makes it return to beginning of loop.
    print(current_number)


#Avoiding INFINITE loops:
#Every while loop needs a way to stop, in order to keep it from running forever.

x = 1
while x <= 5:
    print(x)
    x += 1 #This line adds 1 to x var. every time loop runs, which makes it stop when x hits above 5.

x = 1
# while x <= 5:
#     print(x)
#while loop above will print x value forever, because it will never get above 5 inside loop.
#Press ctrl-c to stop a forever running program.
#Make sure every loop has an exit point.