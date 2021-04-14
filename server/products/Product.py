class Product:
    def __init__(self, name, quantity, restock_date, restock_quantity):
        self.name = name
        self.quantity = quantity
        self.restock_date = restock_date
        self.restock_quantity = restock_quantity

    def getproductDetails(self):
        # empty
        pass 


def updateProductStock():
    # open stock file and reduce by number specified in order
    pass

def getFutureAvailability(product):
    # open orders and sum all orders for a specific file
    # then minus this
    pass