

class Coffee:
    all = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            Coffee.all.append(self)
        else:
            raise ValueError("Coffee name must be at least 3 characters.")

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        from order import Order
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0
