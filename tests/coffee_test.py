import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):

    def setUp(self):
        self.coffee = Coffee("Latte")
        self.customer1 = Customer("Alice")
        self.customer2 = Customer("Bob")
        self.order1 = Order(self.customer1, self.coffee, 4.5)
        self.order2 = Order(self.customer1, self.coffee, 5.0)
        self.order3 = Order(self.customer2, self.coffee, 6.0)

    def test_coffee_has_name(self):
        self.assertEqual(self.coffee.name, "Latte")

    def test_coffee_name_immutable(self):
        with self.assertRaises(AttributeError):
            self.coffee.name = "Mocha"

    def test_coffee_orders(self):
        self.assertEqual(len(self.coffee.orders()), 3)

    def test_coffee_customers(self):
        customers = self.coffee.customers()
        self.assertEqual(len(customers), 2)
        self.assertIn(self.customer1, customers)
        self.assertIn(self.customer2, customers)

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 3)

    def test_average_price(self):
        avg_price = (4.5 + 5.0 + 6.0) / 3
        self.assertAlmostEqual(self.coffee.average_price(), avg_price)

if __name__ == '__main__':
    unittest.main()
