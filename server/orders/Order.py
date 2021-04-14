import json
import csv
import random
import pandas as pd
import datetime

orders_file = "orders.csv"
products_file = "../products/products.csv"

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
    df_products = pd.read_csv(products_file)
    # order details
    product = order.product
    quantity = order.quantity
    # stock details
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
        df_products.to_csv(products_file, index = False, sep=',')
        return "Order Successful, sufficient stock!"
    else:
        return "Sorry, not enough stock to fulfill your order!"


def deleteUserOrder(customer_ID, order_ID):
    df_orders = pd.read_csv(orders_file)
    df_products = pd.read_csv(products_file)

    try:
    # locate the customers order and details
        order = df_orders.loc[(df_orders['customerID'] == customer_ID) & (df_orders['orderID'] == order_ID)]
        product = order['product'].item()
        quantity = order['quantity'].item()

        product_row_num = df_products[df_products['productName'] == product].index[0]
        stock_level = df_products.loc[product_row_num]['stock_quantity']

        # return stock to available
        new_stock_level = stock_level + quantity
        df_products.at[product_row_num, 'stock_quantity'] = new_stock_level
        df_products.to_csv(products_file, index = False, sep=',')

        # delete the order row
        df_orders.drop(order.index, inplace=True)
        # rewrite back to file
        df_orders.to_csv(orders_file, index = False, sep=',')
        return "Success, order successfully deleted"
    except Exception:
        return "Error :("

def localPlaceOrder():
    order_date = datetime.datetime(datetime.datetime.now().year, 3, 1)
    print(placeOrder(Order("user43", "jolt cola", order_date.strftime("%d/%m/%Y"), 200)))


if __name__ == '__main__':
    # print(getUserOrders("user4"))
    print(deleteUserOrder("user43", 97))
    # localPlaceOrder()
