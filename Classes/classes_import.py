#As you add more functionality to your programs, they might get very long and cluttered.
#To solve that, Python lets you store classes in modules, and then import them into your main program!
#You will get same functionality, but your main program will stay nice and clean!


#   Importing a single class:

from car import Car 
#Importing specific class Car from car.py module.
#We can now use it as if it was defined in this file.

my_car = Car('polestar', 'model 2', 2020)
print(my_car.get_descriptive_name())
my_car.odometer_reading = 23
my_car.read_odometer()
print()
#We can use every feature of Car class in here.


#   Storing multiple classes in a module:
#Now, we also added classes Battery and ElectricCar to car.py.

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'roadster', 2021)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print()


#   Importing multiple classes from a module:
from car import Car, ElectricCar

#As you can see above, you can import any amount of classes from a module by separating them with comma.


#   Importing an entire module:
#You can import whole modules by using dot notation like this:
import car

#It's a simple approach that results in easy-to-read code.
# module_name.Classname... syntax.

my_beetle = car.Car('volkswagen', 'beetle', 2015)
print(my_beetle.get_descriptive_name())


#   Importing all classes from a module:

#Following syntax lets you import all classes from a module, without having to call them by dot notation:
# from module_name import *

#NOT A RECOMMENDED METHOD:

#   it doesn't say which classes you're importing.
#   it'll be unclear which classes are from the module.
#   imported classes might confuse python if there are original classes with the same name and so on...

#It's easier to read if you use... module_name.ClassName syntax.


#   Importing a module into a module:

#Sometimes you might want to to spread out your classes over several modules...
# in order to stop a file from growing too large and getting to messy.

#If you find that a class in a module depends on a class in another module...
# you can import the required class into the module.

#In electric_car.py we import Car class, which is necessary in order to use ElectricCar class.


#   Using Aliases:

#When importing modules, you can always give functions, classes or modules nicknames with as-statement.
#Helps you if names are long and tiring to write.

from car import ElectricCar as EC
my_tesla = EC('tesla', 'model x', 2020) #Using alias.
print()


#   The Python Standard Library:

#Python has a standard set of modules that comes with every installation.
#There are lots of standard modules and you can import them as any other module.

#Let's look at the standard 'random' module:
from random import randint
print(randint(1,6)) #randint returns a random number from given range (1-6 in this case).

from random import choice #choice() returns a random value from a list or a tuple.
players = ['drudzi', 'bumba', 'kawze', 'hamlet', 'frozty']
first_up = choice(players)
print(first_up.title())


# Check out Python Module of The Week for standard modules!