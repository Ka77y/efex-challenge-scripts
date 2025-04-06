import unittest
from typing import List
import csv

from src.models.customer import Customer
from src.scripts.the_perfect_arrangement import arrange

class ArrangeTest(unittest.TestCase):
    input_list: List[Customer] = []

    customer_sample_path = "resources/customer_sample.csv"

    def setUp(self):
        self.mock_entry()

    @classmethod
    def mock_entry(cls) -> List[Customer]:
        with open(r'../../resources/customer_sample.csv', encoding="utf-8-sig") as csv_file:
            data = csv.DictReader(csv_file)

            for fila in data:
                customer = Customer(fila["id"], fila["first_name"], fila["last_name"], fila["country"], fila["credit_limit"])
                cls.input_list.append(customer)
    def test_arrange_happy_path(self):
        result = arrange(self.input_list)

        print("\n".join(str(key) for key in result))
