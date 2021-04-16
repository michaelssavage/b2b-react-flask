import json
import csv
import random
import pandas as pd
from datetime import datetime
import threading
from flask import make_response

orders_file = "./orders/orders.csv"
products_file = "./products/products.csv"

class Order:
    def __init__(self, a, customerID, product, date, quantity):
        self.a = a
        self.customerID = customerID
        self.orderID = self.getOrderID(customerID)
        self.product = product
        self.date = date
        self.quantity = quantity

    def toCSV(self):
        order = [self.customerID, self.orderID, self.product, self.quantity, self.date]
        return order

    def getOrderID(self, customerID):
        b = self.a.gen_rlock()
        if b.acquire(blocking=True, timeout=5):
            try:
                df_orders = pd.read_csv(orders_file)
                df_orders.loc[df_orders['customerID'] == customerID]
                numOrders = len(df_orders.index)
                # random method of allocating order number
                orderID = int(numOrders) + random.randint(numOrders + 10, 1000)
                return orderID
            finally:
                b.release()


def getUserOrders(a, customerID):
    b = a.gen_rlock()
    if b.acquire(blocking=True, timeout=5):
        try:
            df = pd.read_csv(orders_file)
            df = df.loc[df['customerID'] == customerID]
            # specify the way to print
            return df.to_json(orient='records')
        except Exception:
            return "No orders for this user :("
        finally:
            b.release()


def deleteUserOrder(a, customerID, order_ID):
    b = a.gen_wlock()
    if b.acquire(blocking=True, timeout=5):
        try:
            df_orders = pd.read_csv(orders_file)
            df_products = pd.read_csv(products_file)

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
            return make_response("Success, order successfully deleted", 200) # Success, order successfully deleted
        except Exception:
            return make_response("Error :(", 409)
        finally:
            b.release()


def getUserOrders(a, customerID):
    b = a.gen_rlock()
    if b.acquire(blocking=True, timeout=5):
        try:
            df = pd.read_csv(orders_file)
            df = df.loc[df['customerID'] == customerID]
            # specify the way to print
            return df.to_json(orient='records')
        except Exception:
            return "No orders for this user :("
        finally:
            b.release()


def placeOrder(a, order):
    # order details
    product = order.product
    quantity = order.quantity
    
    b = a.gen_wlock()
    if b.acquire(blocking=True, timeout=5):
        try:
            # stock details
            df_products = pd.read_csv(products_file)

            product_row_num = df_products[df_products['productName'] == product].index[0]
            stock_level = df_products.loc[product_row_num]['stock_quantity']

            # if order date is in the future after a restock date
            # may need to account for future available stock

            # if order date is between now and before the restock date, use the current stock
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
                return make_response("success", 200)
            else:
                return make_response("failed", 401)
        finally:
            b.release()
