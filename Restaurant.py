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
        
        
        
