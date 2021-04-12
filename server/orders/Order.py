class Order:
    def __init__(self, customer_id, product, date, quantity):
        self.customer_id = customer_id
        self.product = product
        self.date = date
        self.quantity = quantity

    def getOrder(self):
        return("Customer {}, has ordered {} {} on {}".format(self.customer_id, self.quantity, self.product, self.date))

    def cancel_order(self):
        # TODO