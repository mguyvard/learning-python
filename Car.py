class Car:
    '''Describes a simple car'''
    def __init__(self, make, model, year):
        '''Initialize a car'''
        self.make = make
        self.year = year
        self.model = model
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        '''Print a statement showing the car mileage'''
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        '''
        Update the odometer value
        Reject the change if it attemps to roll the odometer back.
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Allows us to increment the mileage"""
        self.odometer_reading += miles

#------------------------------------------------------------------------------

class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size = 76):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"My car has a {self.battery_size}-kwh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 76:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge")

#------------------------------------------------------------------------------

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric car"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self):
        """Electric cars don't have gas tank"""
        print("This car doesn't need a gas tank")


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


my_tesla.battery.get_range()

