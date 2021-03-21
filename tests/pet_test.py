import unittest

from classes.pet import Pet

class TestPet(unittest.TestCase):
    def setUp(self):
    # Set up is a special method that runs before each test
    # Before all of the tests below, this method will run
    # It resets the pet values before each test
        self.pet =  Pet("Sir Percy", "cat", "British Shorthair", 500)

    def test_pet_has_name(self):
        self.assertEqual("Sir Percy", self.pet.name)

    def test_pet_has_type(self):
        self.assertEqual("cat", self.pet.type)

    def test_pet_has_breed(self):
        self.assertEqual("British Shorthair", self.pet.breed)

    def test_pet_has_price(self):
        self.assertEqual(500, self.pet.price)
