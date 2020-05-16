dimensions = (50, 30) #A tuple looks like a list but has parentheses instead of square brackets.
                        #Tuples are immutable, which means the items can't be changed. They are permanent.

print(dimensions[1]) #You can access items in a tuple the same way you do with lists.
print(dimensions[0])
print()

#dimensions[1] = 100 #Trying to change an item inside tuple will give error.

one_item = (10,) #Creating a tuple with only one item will require comma. That defines that it's a tuple.

for i in dimensions: #You can use a for loop just as you do with lists.
    print(i)

#The only way to modify a tuple is by overwriting it, redefining it using a new variable.
print("Original dimensions:")
for i in dimensions:
    print(i)

print("New dimensions:")
dimensions = (100, 200) #Redefining it, giving new values.
for i in dimensions:
    print(i)
