#   EXCEPTIONS
#Python uses special objects called exceptions to manage errors that arise during a program's execution.
#When an error occurs that makes Python unsure what to do next, it creates an EXCEPTION OBJECT.

#You can write your program to handle the exception so your program can continue running when it occurs.
#If you on the other side don't handle the exception in your code, the program will show a traceback which reports the exception that was raised.

#To handle these exceptions, you can use try-except blocks.
#A try-except block tells Python to do something, but also what to do if an exception arises.

#When you use try-except blocks, your programs will keep running even things go wrong...
# and instead of returning tracebacks, it returns your own customized error messages.


#   Handling the ZeroDivisionError exception:

#   print(6 / 0)    #This will of course give an error, because nothing can be divided by 0.
#The trace back returns the ZeroDivisionError, which is an exception object.

#Python creates exception objects in response to a situation where it can't do what we ask it to do.
#When this happens, Python stops the program and tells us what exception was raised.

#Using this information, we can adapt our program and tell Python what to do when this esception occurs.


#   Using try-except blocks:
#When you think of an error that might occur, write a try-except block to handle it.

try: #If the code inside the try block works fine, it skips the except block.
    print(5/0)

except ZeroDivisionError: 
    #If code inside try doesn't work, it searches for an except block that matches the error.
    print("You can't divide by zero!") 
    #When the error above appears it runs this code instead of sending a traceback message.


#   Using Exceptions to prevent crashes:

#Errors often happen in programs prompting for a user input.
#If your program responds to invalid input appropriately, it can ask for more valid input...
# rather than just crashing.

print("Give me two numbers, I'll divide them.")
print("Enter 'q' to quit.")

# while True:
#     first_num = input("\nFirst number: ")
#     if first_num == 'q':
#         break
#     second_num = input("\nSecond number: ")
#     if second_num == 'q':
#         break
#     answer = int(first_num) / int(second_num)
#     print(answer)

#The division above, will error if a number is 0.


#   The else block:
#We could make the loop above more resistant by wrapping the error line in a try-except block.

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("\nSecond number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

#The code above is more stable because it handles the ZeroDivisionError.
# If ZeroDivisionError occurs, it prints a statement.

#The code inside the else block runs only if the try-block was successful.

#By anticipating errors, you can write more robust programs.


#Handling the FileNotFoundError exception:

#A lot of times, you'll run into missing files.
#The files may not exist, be in another directory or is being misspelled.
#Thankfully, you can handle those errors with try-except.

# Let's try to read a file that doesn't exist in same directory:

filename = 'cyka.txt'
# with open(filename, encoding='utf-8') as f:
#    contents = f.read()

#The encoding argument above is needed when your system's default encoding...
# doesn't match the encoding of the file.
#   f is a common variable for representing the file object.

#open() above raises FileNotFound error because it can't find it.

#To handle this error, put open() line inside try-block:

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("Sorry, the file doesn't exist.") #Prints a nice error message if file isn't found.


#   Analyzing text:
#You can analyze text files including entire books, and there are many classical books in txt format.
#Check out Project Gutenberg for more of those books.

#Let's try to count the number of words in Alice in Wonderland:

title = "Alice in Wonderland"
title.split()
#split() method separates a string into parts, whenever if finds a whitespace.
#Then, it stores all the parts in a list.

#We will use split() to get a list of all the words in Alice in Wonderland:

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError: #If file isn't found in try-block it executes code in except-block.
    print(f"Sorry the file '{filename}' does not exist.")
else: #If try-block was successful, it executes else-block.
    words = contents.split()
    words_amount = len(words) #We check length of words list to see how many words it has.
    print(f"The file '{filename}' has about {words_amount} words.")


#   Working with multiple files:
#Let's analyze more books.
#We'll move this bulk of code into a function so we can call it easier:

def count_words(filename):
    """Count the approximate amount of words in a file.""" #Don't forget the docstring!
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError: #If file isn't found in try-block it executes code in except-block.
        print(f"Sorry the file '{filename}' does not exist.")
    else: #If try-block was successful, it executes else-block.
        words = contents.split()
        words_amount = len(words) #We check length of words list to see how many words it has.
        print(f"The file '{filename}' has about {words_amount} words.")

count_words(filename)
print()

#Let's make a loop that prints several different books, from a list:
filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'siddhartha.txt']
for file in filenames:
    count_words(file)
print()

#Even if one file misses, the code will continue because we've handled that exception.
#I deleted siddhartha.txt myself, just to try if it works and it does!
#Boom, that's robust.


#   Failing silently:

#In previous example, we informed user that file wasn't found.
#You don't need to report every exception you catch though.

#Sometimes you'll want programs to fail silently and continue on as if nothing happened.
#To make it fail silently, use pass-statement inside the except block instead of a print statement:

def count_words_silent(filename):
    """Count the approximate amount of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError: #If file isn't found in try-block it executes code in except-block.
        
        pass    #Here we use the PASS STATEMENT to tell Python to do exactly nothing.

    else:
        words = contents.split()
        words_amount = len(words)
        print(f"The file '{filename}' has about {words_amount} words.")

filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'siddhartha.txt']
for file in filenames:
    count_words_silent(file)

#Now, it doesn't inform us about that siddhartha.txt is missing.

#The pass-statement also acts as a placeholder, it's a reminder that you are choosing to do nothing...
# at a specific point in your programs execution and that you might want to do something there later.


#   Deciding which Errors to report:

#Sometimes it'll be hard to know if you should inform users about errors or not.
#Python gives you detailed options to act on based on what you think is right in the situation.
#It's up to you!

#Well-written code, properly tested code, shouldn't be very prone to internal (logic/syntax) errors.
#... if it depends on external information such as a user input or file existence, it may occur errors...
#... it's once again up to you how much to report to users, it comes with experience!



# 10-6. Addition:
print("Please give me two numbers and I'll add them together!")
print("Enter 'q' to quit.")

active = True
while True:
    
    while True:
        first = input("\nFirst number: ")
        if first == 'q':
            active = False
            break
        try:
            num_1 = int(first)    
        except ValueError:
            print("Please enter a numerical value, no text please.")
        else:
            break
    if not active: #This means 'if active = False:'.
        break
    
    while True:
        second = input("Second number: ")
        if second == 'q':
            active = False
            break
        try:
            num_2 = int(second)    
        except ValueError:
            print("Please enter a numerical value, no text please.")
        else:
            break
    if not active: #This means 'if active = False:'.
        break
    
    answer = num_1 + num_2
    print(answer)

#The code above checks if given value is text and if text is anything but 'q' (which stops it)...
# it returns a statement that prompts user to enter a numerical value instead.



# 10-10. Common Words:

def count_word(word, filename):
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    word_appearances = content.lower().count(word.lower())
    #count() finds out how many times a word or phrase appears in a string.
    print(f"Word {word} appears {word_appearances} times in this text.")

count_word('Alice', 'alice.txt')

interesting_words = ['what', 'and', 'is', 'mother', 'scary', 'tired', 'sister']

for word in interesting_words:
    count_word(word, 'alice.txt')