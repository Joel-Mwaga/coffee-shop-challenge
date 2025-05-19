import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order


class TestCustomer(unittest.TestCase):

    def test_customer_init(self):
        customer = Customer("Alice")
        self.assertEqual(customer.name, "Alice")

    def test_customer_name_validation(self):
        with self.assertRaises(Exception):
            Customer("")
        with self.asserRaises(Exception):
            Customer("A" * 16)
        with self.assertRaises(Exception):
            Customer(123)


    def test_create_order(self):
        customer = Customer("Bob")
        coffee = Coffee("Expresso")
        order = customer.create_order(coffee, 3.5)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 3.5)

    def test_customer_orders_and_coffees(self):
        customer = Customer("Carol")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Cappuccino")

        customer.create_order(coffee1, 4.0)
        customer.create_order(coffee1, 4.5)
        customer.create_order(coffee2, 5.0)

        self.assertEqual(len(customer.orders()), 3)
        self.assertEqual(len(customer.coffees()), 2)

if __name__ == '__main__':
    unittest.main()
        