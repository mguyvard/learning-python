import unittest
from city_function import get_city_name

class CityTestCase(unittest.TestCase):
    """Tests for 'city_function.py'."""
    def test_city_country(self):
        """Does it work for 'Santiago, Chile'?"""
        formatted_city = get_city_name("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago, Chile")
        
    def test_city_country_population(self):
        """Does it work for 'Santiago, Chile - population 5_000_000'?"""
        formatted_city = get_city_name("santiago", "chile", 5_000_000)
        self.assertEqual(formatted_city, "Santiago, Chile - Population 5000000")
        
if __name__ == '__main__':
    unittest.main()
