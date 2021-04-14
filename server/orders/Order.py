import json
import csv
import random
import pandas as pd
import datetime

orders_file = "./orders/orders.csv"
products_file = "./products/products.csv"

class Order:
    def __init__(self, customer_id, product, date, quantity):
        self.customer_id = customer_id
        self.order_id = self.getOrderID()
        self.product = product
        self.date = date
        self.quantity = quantity

    def prettyPrint(self):
        return("Customer {}, has ordered {} {} on {}".format(self.customer_id, self.quantity, self.product, self.date))

    def toJSON(self):
        order = {
            "date": self.date,
            "product": self.product,  
            "quantity": self.quantity
        }
        return order

    def toCSV(self):
        order = [self.customer_id, self.order_id, self.product, self.quantity, self.date]
        return order

    # TODO better way of picking order numbers
    # maybe use row count of orders related to cutomer id
    def getOrderID(self):
        num = random.randint(1,100)
        return num

def getUserOrders(customer_id):
    df = pd.read_csv(orders_file)
    try:
        df = df.loc[df['customerID'] == customer_id]
        # specify the way to print
        return df.to_json(orient='records')
    except Exception:
        return "No orders for this user :("


def placeOrder(order):
    df_orders = pd.read_csv(orders_file)
    df_products = pd.read_csv(products_file)

    product = order.product
    quantity = order.quantity

    df_products = df_products.loc[df_products['productName'] == product]
    
    # check if sufficient stock available to filfill order
    if df_products['stock_quantity'].values[0] - quantity > 0:
        return "Order Successful, sufficient stock"
    else:
        return "Sorry, not enough stock to fulfill your order"



    # with open(orders_file, "a", newline="") as orders_csv:
    #     df 
    #     orders_writer = csv.writer(orders_csv, delimiter=',')
    #     orders_writer.writerow(order.toCSV())
    #     return "success"


def deleteUserOrder(customer_ID, order_ID):
    df = pd.read_csv(orders_file)
    try:
        # delete the order row
        df.drop(df.loc[(df['customerID'] == customer_ID) & (df['orderID'] == order_ID)].index, inplace=True)
        # rewrite back to file
        df.to_csv(orders_file, index = False, sep=',')
        return "Success"
    except Exception:
        return "No orders to delete for this user :("


if __name__ == '__main__':
    # print(getUserOrders("user4"))
    # print(deleteUserOrder("user4", 5))

    order_date = datetime.datetime(datetime.datetime.now().year, 3, 1)
    print(placeOrder(Order("user43", "apples", order_date.strftime("%d/%m/%Y"),4000)))
