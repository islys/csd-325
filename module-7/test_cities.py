# Ryan Monnier
# CSD 325
# Module 7 assignmnet
# 16-Feb-2025

# Importing unittest
import unittest
# Importing our city_functions.py which is in the same directory
from city_functions import city_country

# Make a class to use unittest on our function
class TestCityCountry(unittest.TestCase):

    # Defining the test criteria 
    def test_city_country(self):
        # Dictating test parameters for  City, Country, Pop
        result = city_country("Chicago", "USA", population=2000000)
        # setting success criteria
        self.assertEqual(result, "Chicago, USA - population 2000000")
        
        # Test params for City, Country
        result = city_country("Chicago", "USA")
        # setting success criteria
        self.assertEqual(result, "Chicago, USA")
        
        # Test params for City, Country, Pop, and language
        result = city_country("Chicago", "USA", population=2000000, language="English")
        # setting success criteria
        self.assertEqual(result, "Chicago, USA - population 2000000, English")

if __name__ == '__main__':
    unittest.main()
