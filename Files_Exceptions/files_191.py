#   WRITING TO A FILE:

#A simple way to save data, is to write it to a file.
#When writing to a file, the output will still be available after terminal is closed and program is stopped.


#   Writing to an Empty File:
filename = 'programming.txt'

with open(filename, 'w') as file_object:
#open() loads the filename to alias file_object.
#Second argument 'w' in open()-call tells Python to open the file in writing-mode.
    file_object.write("I love programming.") #You can now use write() to write inside given file.

#Check what has happened to programming.txt!

#You can open a file in: (most common)
#   read-mode ('r') <--- THIS IS DEFAULT
#   write-mode ('w')
#   append-mode ('a')
#   read-and-write-mode ('r+)
#   creates new file and write to it ('x')

#open() automatically creates a new file if it doesn't already exist in your directory.
#Be careful using 'w' if you're not certain that your file doesn't exist, because Python overwrites it.
#If you want to make sure that you're creating a new file, use 'x'.

#Python can only write strings to text files, if you want to write numerical data, reformat to str with str().


#   Writing multiple lines:
#write() doesn't add any newlines to your text, for it to write in multiple lines...
#   use newline characters:

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
#If you open programmin.txt now, you'll see the two lines above squished together in one line.

#Now, we include newline character, so each string appears in separate line:
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")


#   Appending to a file:
#If you want to add content to a file without overwriting what already is...
#   open the file in append mode ('a').
#Append mode won't erase content, it will add it to the end of the file.

#If the given file doesn't exist, Python will create an empty file for you just like when using 'w'.

filename = 'programming.txt'
with open(filename, 'a') as file_object: #We open the file in append-mode.
    file_object.write("I also love finding meaning in large datasets.\n") #write() now adds string to the end of the file you're working with.
    file_object.write("I love creating apps that can run in a browser.\n")
    file_object.write("I love to make fuckboy-games!")

#Run program and check new lines in the file!
#New lines are added at the bottom!



# 10-4. Guest Book:
guest_book_file = '10_4_guestbook.txt'
with open(guest_book_file, 'a') as guest_book:
    while True:
        name = input("\nEnter quit if you'd like to stop.\nWhat's your name? ")
        if name.lower() == 'quit':
            break
        else:
            print(f"Hello, {name.title()}!")
            guest_book.write(f"{name.title()} was here!\n")