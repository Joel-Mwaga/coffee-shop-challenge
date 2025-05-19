

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        from order import Order
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
   
@classmethod
def most_aficionado(cls, coffee):
    from order import Order
    customers = {}
    for order in Order.all:
        if order.coffee == coffee:
            customers[order.customer] = customers.get(order.customer, 0) + order.price
    if customers:
        return max(customers, key=customers.get)
    return None

    

