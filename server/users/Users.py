import threading
import pandas as pd
import csv

orders_file = "./orders/orders.csv"
lock = threading.Lock()

class Users:
    def __init__(self, name, password):
        self.name = name
        self.password = password


def add_new_customer(customerID, password):
    lock.acquire()
    df_users = pd.read_csv('./users/users.csv')
    # get the id column
    df_users = df_users.loc[df_users['userID'] == customerID]

    # if no matches found
    if df_users.empty:
        with open("./users/users.csv", "a", newline="") as users_csv:
            orders_writer = csv.writer(users_csv, delimiter=',')
            orders_writer.writerow([customerID, password])
            lock.release()
        return "User successfully added"
    # otherwise username already present
    else:
        lock.release()
        return "User already exists"