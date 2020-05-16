#   WORKING WITH CLASSES AND INSTANCES:

#   The car class:
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


my_car = Car('tesla', 'cybertruck', 2020)
print(my_car.get_descriptive_name())
my_car.read_odometer()


#   Modifying Attribute Values:

#Modifying an attribute's value directly:
my_car.odometer_reading = 23 #We use dot notation to access instance attributes.
#Python finds attribute in instance, and sets the new value.
my_car.read_odometer() 


#Modifying an attribute's value through a method:
#Instead of accessing attribute directly,
#... you can pass new value to a method updating it internally.

# def update_odometer(self, mileage):
#         """
#         Set the odometer to given value.
#         Reject the change if it attempts to roll back the odometer.
#         """
#         if mileage >= self.odometer_reading:    
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll the odometer back!")

my_car.update_odometer(167) #Added this method to Car class.
my_car.read_odometer()


# Incrementing an attribute's value through a method:
#Sometimes we want to increase a value, without giving a completely new value.

# def increment_odometer(self, miles):
#         """Add given amount to the odometer reading."""
#         self.odometer_reading += miles 
my_car.increment_odometer(553) #Adds 553 miles to the odometer.
my_car.read_odometer()

