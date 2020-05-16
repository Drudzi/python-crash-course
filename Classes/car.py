"""A set of classes that can be used to model a gas- and electric cars."""

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


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific for an electric car.
        """
        super().__init__(make, model, year) 
        self.battery = Battery(100)

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")