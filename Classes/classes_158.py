#When you write a class, you define the general behaviour... 
#...that a whole category of objects can have.
#You can model almost anything using classes.



#   CREATING AND USING A CLASS:

#Simple class representing any dog:
class Dog: #By convention, capitalized names refer to classes in Python.
    """A simple attempt to model a dog.""" #Always write docstring to say what class does.

#A function that's a part of a class is called a method.
    def __init__(self, name, age): #This defines METHOD __init__.
        # self parameter is required in __init__ and should be placed first.
        #Whenever an instance (object) is created using the class, it runs __init__.
        """Initialize name and age attributes."""
        self.name = name #Variable prefixed with self is available to every method in class.
        self.age = age #They are also called attributes.
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")

#Look at self as kind of a pointer towards the actual __init__ method.
#Think of a class as a set of instructions for how to make an instance (object).


#    Making an instance from a Class:

#Instance representing the dog "Willie":
my_dog = Dog('Willie', 6) #The __init__ method sets attributes for name and age as we...
#...make the instance using the class.
print(f"My dog's name is {my_dog.name}.") 
print(f"My dog is {my_dog.age} years old.")


#   Accessing Attributes:
#To access the attributes of an instance, you use dot notation.

#We access the dog's name writing:
my_dog.name
my_dog.age


#   Calling Methods:
my_dog = Dog('Willie', 7) #Creating instance from Dog class.
#After an instance is created, we can call any method from that class using dot notation.

my_dog.sit() #Calls sit() method from Dog class.
my_dog.roll_over() #Calls roll_over() method from Dog class.


# Creating Multiple Instances:
#You can create as many instances as you want from a class.

your_dog = Dog('Lucy', 4)
his_dog = Dog('Nellie', 9)

print(f"My dog's name is {my_dog.name}.")
print(f"Your dog's name is {your_dog.name}.")
print(f"His dog's name is {his_dog.name}.")

my_dog.sit()
your_dog.sit()
his_dog.sit()
print()


#   9-3. Users:
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

my_profile = User('jonathan', 'axelsson', 'Drudzi', 18)
my_profile.describe_user()
my_profile.greet_user()