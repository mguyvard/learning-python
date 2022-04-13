class Employee:
    def __init__(self, first_name, Last_name, annual_salary):
        self.first_name = first_name.title()
        self.Last_name = Last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, default_increase = 5_000):
        self.annual_salary += default_increase
        return self.annual_salary
    
    


