import unittest 
from Employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        """Creates an instance of the Employee class"""
        self.my_employee = Employee("frank", "salou", 90_000)
        
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(95_000, self.my_employee.annual_salary)
        
    def test_give_custom_raise(self):
        self.my_employee.give_raise(3_000)
        self.assertEqual(93_000, self.my_employee.annual_salary)
        
if __name__ == "__main__":
    unittest.main()
