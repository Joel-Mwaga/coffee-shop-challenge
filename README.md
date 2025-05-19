# ☕ Coffee Shop Challenge

This is a Python OOP project simulating a coffee shop system with three main models: **Customer**, **Coffee**, and **Order**.

## Relationships

- A **Customer** can place many **Orders**
- A **Coffee** can have many **Orders**
- An **Order** belongs to both one **Customer** and one **Coffee**

This forms a many-to-many relationship between Customer and Coffee, using Order as the join model.

## 🔧 Features

- Enforces proper data types and constraints on initialization
- Read-only properties for immutable data like coffee name and order price
- Tracks all orders for each customer and coffee
- Provides aggregates such as average coffee price and number of orders
- Includes class method to find the biggest spender on a specific coffee

## 🧪 Testing

Unit tests are provided for all classes under the `/tests` directory:

```bash
python tests/customer_test.py
python tests/coffee_test.py
python tests/order_test.py
```

## 📁 Project Structure

```
coffee-shop-challenge/
├── Pipfile
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
    ├── customer_test.py
    ├── coffee_test.py
    └── order_test.py
```

## 🚀 Setup Instructions

Clone the repo:

```bash
git clone git@github.com:<your-username>/coffee-shop-challenge.git
cd coffee-shop-challenge
```

Create and activate your environment:

```bash
pipenv install
pipenv shell
```

Run the tests or the debug script to explore the code:

```bash
python debug.py
```
