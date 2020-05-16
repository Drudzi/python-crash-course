numbers = list(range(1,6)) #List function turns numbers in range into list, making list functions usable on it.
even_numbers = list(range(2,11,2)) #This outputs every even number from 1-10. The third input in range decides step size between numbers.

squares = []
for value in range(1,11): #This for loop collects every square from 1-10 and stores them in variable squares.
    # square = value ** 2 #Squares every value in the range.
    # squares.append(square) #Adds the square to the end of the squares-list with append.
    squares.append(value**2) #This is a more concise way, instead of the two above. Directly appends whatever value to the power of two.
#print(squares)

squares = [value**2 for value in range(1,11)] #This is a LIST COMPREHENSION. Combines a for loop and the creation of 
                                                #new elements, and automatically appends each new element.

#Following functions can find maximum, minimum and sum of a list:
numbers_2 = range(1,101)
(min(numbers_2))
(max(numbers_2))
(sum(numbers_2))

#Multiples of 3 from 3 to 30:
threes = list(range(3,31,3))

#10 first cubes:
cubes = []
for value in range(1,11):
    cubes.append(value**3)
#cubes = [value**3 for value in range(1,11)] COMPREHENSIVE LIST WAY
print(cubes)