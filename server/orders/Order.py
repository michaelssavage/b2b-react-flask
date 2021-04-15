import json
import csv
import random
import pandas as pd
import datetime
import threading

orders_file = "./orders/orders.csv"
products_file = "./products/products.csv"

# shared lock object
lock = threading.Lock()

class Order:
    def __init__(self, customerID, product, date, quantity):
        self.customerID = customerID
        self.orderID = self.getOrderID(customerID)
        self.product = product
        self.date = date
        self.quantity = quantity

    def toCSV(self):
        order = [self.customerID, self.orderID, self.product, self.quantity, self.date]
        return order

    def getOrderID(self, customerID):
        df_orders = pd.read_csv(orders_file)
        df_orders.loc[df_orders['customerID'] == customerID]
        numOrders = len(df_orders.index)
        # random method of allocating order number
        orderNum = int(numOrders) + random.randint(numOrders + 10, 1000)
        return orderNum


def deleteUserOrder(customerID, order_ID):
    lock.acquire()

    df_orders = pd.read_csv(orders_file)
    df_products = pd.read_csv(products_file)

    try:
        # locate the customers order and details
        order = df_orders.loc[(df_orders['customerID'] == customerID) & (df_orders['orderID'] == order_ID)]
        product = order['product'].item()
        quantity = order['quantity'].item()

        product_row_num = df_products[df_products['productName'] == product].index[0]
        stock_level = df_products.loc[product_row_num]['stock_quantity']

        # return cancelled stock to available
        new_stock_level = stock_level + quantity
        df_products.at[product_row_num, 'stock_quantity'] = new_stock_level
        df_products.to_csv(products_file, index = False, sep=',')

        # delete the order row
        df_orders.drop(order.index, inplace=True)
        # rewrite back to file
        df_orders.to_csv(orders_file, index = False, sep=',')
        lock.release()
        return "success" # Success, order successfully deleted
    except Exception:
        lock.release()
        return "failed" # Error :(


def getUserOrders(customerID):
    df = pd.read_csv(orders_file)
    try:
        df = df.loc[df['customerID'] == customerID]
        # specify the way to print
        return df.to_json(orient='records')
    except Exception:
        return "No orders for this user :("


def placeOrder(order):
    # order details
    product = order.product
    quantity = order.quantity

    print(product, quantity)
    # acquire lock
    lock.acquire()
    # stock details
    df_products = pd.read_csv(products_file)

    product_row_num = df_products[df_products['productName'] == product].index[0]
    stock_level = df_products.loc[product_row_num]['stock_quantity']

    # check if sufficient stock available to filfill order
    if stock_level - quantity >= 0:
        # add order to orders file
        with open(orders_file, "a", newline="") as orders_csv:
            orders_writer = csv.writer(orders_csv, delimiter=',')
            orders_writer.writerow(order.toCSV())

        # update stock
        new_stock_level = stock_level - quantity
        df_products.at[product_row_num, 'stock_quantity'] = new_stock_level
        # update value on file
        df_products.to_csv(products_file, index = False, sep=',')
        # release the lock
        lock.release()
        return "success"
    else:
        lock.release()
        return "failed"
