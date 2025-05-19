import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Test Customer")
        self.coffee = Coffee("Espresso")

    def test_valid_order_creation(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

    def test_invalid_customer_type(self):
        with self.assertRaises(TypeError):
            Order("NotACustomer", self.coffee, 5.0)

    def test_invalid_coffee_type(self):
        with self.assertRaises(TypeError):
            Order(self.customer, "NotACoffee", 5.0)

    def test_price_must_be_float(self):
        with self.assertRaises(TypeError):
            Order(self.customer, self.coffee, "5")

    def test_price_range_too_low(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.99)

    def test_price_range_too_high(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 10.5)

    def test_price_immutable(self):
        order = Order(self.customer, self.coffee, 5.0)
        with self.assertRaises(AttributeError):
            order.price = 8.0

if __name__ == '__main__':
    unittest.main()
