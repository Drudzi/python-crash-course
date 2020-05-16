#Working with files will make your programs more relevant and usable.
# it enables you to analyze and store lots of data.  


#   READING FROM A FILE:

#In text files, there are lots of data.
#Reading from files can be very useful, for an example, you can do data analysis or modifying data.

#To be able to work with text files, you first need to read it into memory:


#   Reading an entire file:
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# open() function in first line opens the file given as a string in the arguments.
# For it to open the file, it needs to be stored in the same directory.
# The open() function returns an object representing the given file.

#We nickname pi_digits.txt file_object using as (alias).
#Then, we store a long string of the txt file in variable contents using read() method.
#When we print contents, we print what's in the txt file.

# Keyword 'with' in the first line closes the file when you no longer need access to it.
# with figures it out automatically for you when with block finishes execution.

#You can also close it manually in your code using close() method, but if it's used incorrectly...
# it can cause bugs, errors, data losses or corruptions.

#read() always returns an empty string when it reaches to end of a text file.
# If you want to remove this blank line, use rstrip():
print(contents.rstrip())


#   File Paths:
#Sometimes you might want to access files in another directory.
#To do that, you need to provide a 'relative file path'.

#Consider your text files being in another folder called text_files:
#   with open('text_files/filename.txt') as file_object:
# Folder text_files should be located in same directory as your python file.

#If you want to access any file on your computer, you can use 'absolute file paths'.
#Absoulute file paths are usually longer, so it's valueable to store them in variables:

#Remeber to use either forward slashes (/) or double backslashes (\\) when entering directories...
# because a single backslash (\) is used to escape characters in strings. Ex) \n for a new line.


#   Reading line by line:
#Sometimes you'll want to examine each line of a file.
#You might want to look for certain information or modify some text.

# Example: You might want to look through weather data and work with any line including word 'sunny'.

#You can use FOR LOOPS to examine each line in a file one at a time:
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object: #When looping through a file, it loops over the lines in the file.
        print(line)

#This will give a blank line between every line, use rstrip() to not get them.


#   Making a list of lines from a file:
#To retain access to a file's contents after with block...
# you can store the lines of the file in a list inside the with block and then work with that list:

with open(filename) as file_object:
    lines = file_object.readlines() #readlines() takes stores every line as items in a list.

for line in lines:
    print(line.rstrip())
print()

print(lines[0]) #Printing first line in file.


#   Working with a file's contents:
#When you've read file into memory, you can do pretty much anything with it.
#Let's try to build a string of all digits in pi, without whitespaces:
pi_string = ''
for line in lines:
    pi_string += line.strip() #Adding every line to string.
    #If you use rstrip, it will contain the whitespaces that are in front of every row in the file.
    #To solve that, use strip() instead, it takes out whitespaces on both sides.

pi = float(pi_string) #If you want to work with it numerically you can convert it to float or integer.
print(pi_string)
print(len(pi_string))


#   Large files: One million digits
#Python has no file size limit, you can work with as large files as your system can handle.

filename = "pi_million_digits.txt"
with open(filename) as file_object: #Loading file with 1 million digits of pi.
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...") #Printing only first 50 decimals.
print(len(pi_string))


#   Is your birthday contained in Pi?

birthday = input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string: #We check if birthday-string appears inside of pi-string.
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear in the first million digits of pi.")

#Once you've read the file into your program, you can analyze its content in many ways.