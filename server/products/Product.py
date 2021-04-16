import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

orders_file = "./orders/orders.csv"
products_file = "./products/products.csv"

class Product:
    def __init__(self, name, quantity, restock_date, restock_quantity):
        self.name = name
        self.quantity = quantity
        self.restock_date = restock_date
        self.restock_quantity = restock_quantity


def getproducts(a):
    # read lock
    b = a.gen_rlock()
    if b.acquire(blocking=True, timeout=5):
        try:
            # read file and return as json
            df_products = pd.read_csv("./products/products.csv")
            return df_products.to_json(orient='records')
        finally:
            b.release()


def getFutureAvailability(a, product, time):
    b = a.gen_rlock()
    if b.acquire(blocking=True, timeout=5):
        try:
            # set the cut off date for x months from now
            cutOffDate = date.today() + relativedelta(months=+time)

            # read the files
            df_orders = pd.read_csv(orders_file)
            df_products = pd.read_csv(products_file)

            # format the dates correctly for comparison
            df_orders['date'] = pd.to_datetime(df_orders['date'], format="%d/%m/%Y").dt.date
            # filter dates for orders within the specified time range
            df_orders = df_orders.loc[df_orders['date'] <= cutOffDate]

            # get the rows for the product in the product and orders file
            df_products = df_products.loc[df_products['productName'] == product]
            df_orders = df_orders.loc[df_orders['product'] == product]

            # need to compare this with the stock and restocking rate
            product_row_num = df_products[df_products['productName'] == product].index[0]
            stock_level = df_products.loc[product_row_num]['stock_quantity']

            productRestockQuantity = df_products.loc[product_row_num]['restock_quantity']
            restockingForThisPeriod = productRestockQuantity * time

            # stock level already accounts for current orders
            projectedAvailability = stock_level + restockingForThisPeriod
            return int(projectedAvailability)
        except Exception as e:
            return e
        finally:
            b.release()
