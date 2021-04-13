import json

class Order:
    orders_file = "orders.json"

    def __init__(self, customer_id, product, date, quantity):
        # self.order_id = 
        self.customer_id = customer_id
        self.product = product
        self.date = date
        self.quantity = quantity

    def getOrder(self):
        return("Customer {}, has ordered {} {} on {}".format(self.customer_id, self.quantity, self.product, self.date))

    def toJSON(self):
        order = {
            "date": self.order_date,
            "product": self.product,  
            "quantity": self.quantity
        }

        return order

    def getItems(self, orders_list=None):
        try:
            with open(orders_file, "r") as json_file:
                data = json.load(json_file)
                if orders_list != None:
                    return data[orders_list]
                else:
                    return data
        except IOError:
            print(f"Could not read file {orders_file}")
            return None

    def addItem(self, item, orders_list):
        data = self.getItems()
        
        #orders_list is either urlSet or tagSet
        if item not in data[orders_list]:
            data[orders_list].append(item)
            self.dumpItems(data)
        # else:
        #     print(f"{item} already in {orders_list}")

    def cancelOrder(self, item, orders_list):
        data = self.getItems()
        try:
            data[orders_list].remove(item)
            self.dumpItems(data)
        except ValueError:
            print(f"{item} not in {orders_list}")

    def dumpItems(self, data):
        with open(orders_file, "w") as json_file:
            json.dump(data, json_file, indent=4, sort_keys=True)


def search_price():
    with open("orders.json", "r") as json_file:
        data = json.load(json_file)
        print(data['user42'])

    # for keyval in data:
        # print(keyval)
        # print(list(filter(lambda x:x["author"]=="Nikolaos Gkikas",keyval)))


    #     if name.lower() == keyval['name'].lower():
    #     return keyval['unit_price']

    # # Check the return value and print message
    # if (search_price(item) != None):
    # print("The price is:", search_price(item))
    # else:
    # print("Item is not found")

                
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

if __name__ == '__main__':
    search_price()