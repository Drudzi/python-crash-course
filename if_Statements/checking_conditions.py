car = "audi" #A single equal sign sets the value of a variable to given value.
car == "bmw" #Double equal signs asks if value in a variable equals a given value. Returns either True or False.

car = "Audi"
car == "audi" #This returns false because capitalization is different.
car.lower() == "audi" #This trick will temporarily convert value of car into lowercase before comparing it. Solves capitalization problem. 

#Checking for inequality:
car = "volvo"
car != "audi" # != means "not." If car is not equal "audi", it returns True.

if car != "audi":
    print("That's no Audi")

#Numerical:
age = 18
age == 18 #Returns True. Works just like with strings.
age < 21 #You can use mathematical comparisons as well. Returns True, because 18 is less than 21.
age > 21 #Returns False.
age <= 21 #Returns True.
age >= 21 #Returns False.

#Multiple conditions:
age_1 = 18
age_2 = 20
(age_1 <= 20) and (age_2 <= 20) #And checks both conditions, if both passes it returns True. If any or both are False, it returns False.
#Parentheses above aren't required, but improves readability.

(age_1 < 20) or (age_2 < 20) #"or" checks if any of given conditions pass. If any pass, it returns True. Returns False if none pass.

#Checking whether a value is in a list:
cars = ["audi", "bmw", "volvo", "polestar", "tesla"]
"tesla" in cars #Will give True because Tesla is in list.
"ferrari" in cars #Will give False because Ferrari isn't in list.

#Checking whether a value is not in a list:
"tesla" not in cars #Will give False becuase Tesla is in list.
"ferrari" not in cars #Will give True because Ferrari is not in list.

banned_cars = ["fiat", "bugatti", "ford"]
car = "toyota"
if car not in banned_cars:
    print("You are free to drive your " + car.capitalize() + "!")
else:
    print("Turn around!")

#Boolean expressions:
game_active = True #Booleans are often used for tracking certain states. Game is still going.
can_edit = False #User cannot edit.