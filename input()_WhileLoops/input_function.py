#input() function pauses your program until it recieves an input from the user.
message = input("Tell me something, and I will repeat it back to you: ") #input() stores given data in variable message.
print(message) #Prints what was given from user.

print(input("Does this work? ")) #After an input from user, code: input("Does this work? ") will be treated as any string.


#Writing Clear Prompts:
#When using input() function, always include a clear and easy-to-follow prompt.
#Tell the user exactly what kind of data you want.
name = input("Please enter your name: ") #Here, it's clear and easy to understand what to enter.
#Use space between last character in input() and last " to separate prompt from user input.
print(f"\nHello, {name.title()}!") 

#Long prompts:
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your name? " # += adds data directly at the end of data inside variable.
name = input(prompt)
print(f"Hello, {name.title()}!")


#Using int() to accept numerical input:
age = input("How old are you? ") #Any number or letters will be returned in a string, not numerical.
#age <= 18 #This gives error because you cant include strings in numerical comparisons (math).
#age var. needs to be considered a number.

age = int(age) #int() turns data into an integer (number). You can also use float().
#int() can only turn string with a number into integer. If letters in age var. it gives error.
if age < 18:
    print("This is a number (data type).")