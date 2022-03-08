class Restaurant:
    """A simple class describing a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant"""
        msg = f"\nThe {self.name} is a {self.cuisine_type} restaurant"
        print(msg)

    def open_restaurant(self):
        """Indicate that the restaurant is open"""
        msg = f"\nThe {self.name} is open now"
        print(msg)

    def set_number_served(self, number_served):
        """Allows to set the number of clients served"""
        self.number_served = number_served

    def increment_number_served(self, increment):
        '''Allows to increment the number of clients served'''
        self.number_served += increment
        return self.number_served


class IceCreamStand(Restaurant):
    """Child class inherits from the Restaurant class"""

    def __init__(self, name, cuisine_type="ice cream"):
        """Initialize attributes of the parent class"""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """Print the list of flavors"""
        print("\nFlavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


my_restaurant = Restaurant("le rivioli", "french")
my_restaurant.describe_restaurant()
iceCreamStand = IceCreamStand("marriot")
iceCreamStand.describe_restaurant()
iceCreamStand.flavors = ["banana", "vanilla", "chocolate", "passion fruit"]
iceCreamStand.display_flavors()


