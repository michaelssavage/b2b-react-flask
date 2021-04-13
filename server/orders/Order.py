import json
import csv
import random

orders_file = "./orders/orders.csv"

class Order:

    def __init__(self, customer_id, product, date, quantity):
        self.customer_id = customer_id
        self.order_id = self.getOrderID()
        self.product = product
        self.date = date
        self.quantity = quantity

    def getOrder(self):
        return("Customer {}, has ordered {} {} on {}".format(self.customer_id, self.quantity, self.product, self.date))

    def toJSON(self):
        order = {
            "date": self.date,
            "product": self.product,  
            "quantity": self.quantity
        }

        return order

    def toCSV(self):
        order = [self.order_id, self.customer_id, self.product, self.quantity, self.date]
        return order

    # TODO better way of picking order numbers
    def getOrderID(self):
        num = random.randint(1,100)
        return self.customer_id + str(num)

def getUserOrders(customer_id):
    with open(orders_file, "r") as orders_csv:
        try:
            data = json.load(orders_csv)
            return data[customer_id]
        except Exception:
            return "No orders for this user :("

def placeOrder(order):
    with open(orders_file, "a", newline="") as orders_csv:
        orders_writer = csv.writer(orders_csv, delimiter=',')
        orders_writer.writerow(order.toCSV())
        return "success"

                
# Order Schema:
#     {
#     "user42": [
#         {
#             "date": "14/02/2021",
#             "product": "game boy",  
#             "quantity": 2
#         },
#         {
#             "date": "04/03/2021",
#             "product": "game boy",  
#             "quantity": 2
#         }
#     ]
# }


# if __name__ == '__main__':
#     search_price()