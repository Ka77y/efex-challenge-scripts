import unittest
from src.floor_calculator import floor


class FloorCalculatorTest(unittest.TestCase):
    def test_floor_happy_path(self):
        result = floor(2.3, 1.9)
        self.assertEqual(result, 4)
