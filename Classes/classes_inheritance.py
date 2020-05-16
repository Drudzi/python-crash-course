#You don't always have to write a new class from scratch.
#If class you're writing is a specialized version of another class...
#...USE INHERITANCE.
#When you inherit a class from another you're making a child class of a parent class.


#   The __init__() method for a Child Class:
#Let's use Car class as an example:
#Continuing after Class definition.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        #These are the initial attributes it needs:
        self.make = make
        self.model = model
        self.year = year
        #Attributes don't have to be passed as parameters.
        #They can be assigned default values in __init__ method.
        self.odometer_reading = 0 #Adds new attribute that has a default value.

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odometer to given value.
        Reject the change if it attempts to roll back the odometer.
        """
        if mileage >= self.odometer_reading:    
            self.odometer_reading = mileage
        else:
            print("You can't roll the odometer back!")
    
    def increment_odometer(self, miles):
        """Add given amount to the odometer reading."""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """Simulate filling the gas tank."""
        print(f"Filling the gas tank of your {self.make.title} {self.model.title}.")


#Let's say we wan't to model an electric car, which is a type of car:
#We can use Car class as a parent class. 
#To make a child class, the parent class must be in your file and appear before.

class ElectricCar(Car): #Defining child class ElectricCar.
                        #Name of parent class should be included inside parentheses.
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): #This __init__ takes in the required...
                                    #...information to make a Car instance.
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific for an electric car.
        """
        super().__init__(make, model, year) #super() allows you to call methods from the parent class.
        #super() calls __init__ from parent class.
        #Name SUPER comes from a convention calling parent classes superclasses and child classes subclasses.
        self.battery_size = 75 #Initializing battery_size attribute.
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model x', 2020) #Making an instance of ElectricCar and storing it in my_tesla.

# ElectricCar('tesla', 'model x', 2020) calls __init__ in ElectricCar which in turn calls __init__ in Car.

print(my_tesla.get_descriptive_name()) #Now, we can access methods inside parent class Car.


#   Defining attributes and methods for the Child Class:
#Once child class is created, you can add any attributes and methods you want.

#In the definition, I add a new attribute called battery_size and a new method called describe_battery().
my_tesla.describe_battery() #Describing battery size. 
# There is no limit to how much you can specialize!

#Think about not adding methods and attributes that any type of car can have to a child class like ElectricCar.
#If you want to add number of horsepowers, it's better to add it to the parent class Car.
#Then you have that attribute in all child classes you make.


#   Overriding Methods from the Parent Class:
#You can override methods from the parent class if it doesn't match what you want it to do in the child class.

#To do this,
# you define new method in child class with the same name as the method in the parent class you wanna override.

#I modified fill_gas_tank() method in ElectricCar child class, because an electric car doesn't have a gas tank.
my_tesla.fill_gas_tank()


#   Instances as Attributes:
#When making a class, you might end up with a lot of methods and attributes for one specific thing...
# then, you can make a new class of this thing with all of its attributes and methods.
#You can use an instance of the new class to represent the the specific thing in the primary class.

# ex) We can make a class called Battery, representing the car's battery and make an instance of it...
#     that we put in the Car class:

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75): #Takes values for battery size, but has a default 75.
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    
class ElectricCar_1(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific for an electric car.
        """
        super().__init__(make, model, year) 
        self.battery = Battery(100) #Creating instance of Battery inside ElectricCar class.
        #Assigns instance to attribute self.battery.
        #Any instance of ElectricCar_1 now has a Battery instance created automatically.

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar_1('tesla', 'model x', 2020)
my_tesla.battery.describe_battery() #Now, we can use methods from Battery() in ElectricCar_1 instances.
my_tesla.battery.get_range()
#The benefit of this, is that we can now detail the battery as much as we want...
#...without cluttering ElectricCar class.
print()



# 9-8. Admin Privileges:
class User:
    """Attempt representing a user."""
    def __init__(self, first_name, last_name, username, age):
        """Initialize attributes to describe user."""
        self.first = first_name
        self.last = last_name
        self.username = username
        self.age = age

    def describe_user(self):
        """Describe user's attributes."""
        print(f"Information about user: {self.username}")
        print(f"First name: {self.first.title()}")
        print(f"Last name: {self.last.title()}")
        print(f"Age: {self.age}")

    def greet_user(self):
        """Print a greeting message to user."""
        print(f"Hello, {self.first.title()}")

admin_privileges = ['cad add post', 'can delete post', 'can ban user', 'can delete user', 'can modify user']

class Privileges:
    """Represent privileges of a User."""
    def __init__(self, privileges):
        """Initialize user's privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """Print a statement, showing privileges."""
        print("Privileges:")
        for i in self.privileges:
            print(i.title())


class Admin(User):
    """Represent an Admin."""
    def __init__(self, first_name, last_name, username, age):
        """Initialize Admin's attributes and its privileges."""
        super().__init__(first_name, last_name, username, age)
        self.privileges = Privileges(admin_privileges)


my_user = Admin('jonathan', 'axelsson', 'drudzi', 18)
my_user.privileges.show_privileges()