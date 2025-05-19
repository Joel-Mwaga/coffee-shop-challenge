from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice.create_order(latte, 3.5)
alice.create_order(espresso, 4.0)
bob.create_order(latte, 2.5)
bob.create_order(latte, 5.0)

print("Alice's Orders:")
for order in alice.orders():
    print(f"- {order.coffee.name}: ${order.price}")

print("\nCoffees Alice has tried:")
for coffee in alice.coffees():
    print(f"- {coffee.name}")

print("\nLatte Orders:")
for order in latte.orders():
    print(f"- {order.customer.name}: ${order.price}")

print("\nCustomers who ordered Latte:")
for customer in latte.customers():
    print(f"- {customer.name}")

print(f"\nNumber of Late orders: {latte.num_orders()}")

print(f"Average Late price: ${latte.average_price():.2f}")
