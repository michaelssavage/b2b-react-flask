import pandas as pd

class Product:
    def __init__(self, name, quantity, restock_date, restock_quantity):
        self.name = name
        self.quantity = quantity
        self.restock_date = restock_date
        self.restock_quantity = restock_quantity

def getproducts():
    # read file and return as json
    df_products = pd.read_csv("./products/products.csv")
    return df_products.to_json(orient='records')


def updateProductStock():
    # open stock file and reduce by number specified in order
    pass

def getFutureAvailability(product):
    # open orders and sum all orders for a specific file
    # then minus this
    pass