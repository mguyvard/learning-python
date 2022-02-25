class Car():
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
        print(f"Thic car has {self.odometer_reading} miles on it")
        
    def update_odometer(self, mileage):
        '''
        Update the odometer value
        Rreject the change if it attemps to roll the odometer back.
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
        
    def  increment_odometer(self, miles):
        '''Add the given amount to the odometer reading'''
        self.odometer_reading += miles
    
class ElectricCar(Car):
     '''Represent aspects of a car, specific to electric cars'''
     def __init__(self, make, model, year):
         """Initializes attributes of the parent class.
         Then initializes attributes specific to electric cars
         """
         super().__init__(make, model, year)
         self.battery_size = 75  
     def describe_battery(self):
        '''Print a statement describing the battery size'''
        print(f"This car has a battery size of {self.battery_size}-kWh battery")

        
my_tesla = ElectricCar("tesla","model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.update_odometer(45)
my_tesla.increment_odometer(52)

print(my_tesla.read_odometer())       
         