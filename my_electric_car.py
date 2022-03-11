from car import ElectricCar

my_tesla = ElectricCar('model s', 'a4', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.odometer_reading = 23
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


