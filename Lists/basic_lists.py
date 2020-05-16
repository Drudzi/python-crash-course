cars = ["volvo", "tesla", "audi", "bmw"]
cars.append("porsche") #Adds element in end of list.
cars.append("toyota")
cars.insert(0, "polestar") #Inserts at index, moves other elements one right.
cars[3] = "honda"
print(cars)
print()
cars.sort() #Sorts cars in alphabetical order.
print(cars)

message = f"\nMy first car was a {cars[0].title()}!"
print(message)
print()
cars.sort(reverse=True) #Sorts in reverse alphabetical order.
print(cars)
print()

last_car = cars.pop() #Pops an item at given index (default = last).
print(last_car)

del cars[1] #Deletes an item at an index position.
cars.remove("tesla") #Removes item by given name.
too_expensive = "porsche"
cars.remove(too_expensive)
print()
print(cars)
print(f"\nA {too_expensive.title()} is too expensive for me!")

print("This is the original order of the list: ")
print(cars)
print()
print("This is the sorted list: ")
print(sorted(cars)) #sorted() temporarily sorts a list.
print()
cars.reverse() #Reverses the order of a list.
print("This is the original order, but reversed: ")
print(cars)
print()
print("The number below shows the number of cars in the list: ")
print(len(cars)) #len() views number of elements in list.