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
        