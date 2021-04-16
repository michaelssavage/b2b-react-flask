import threading
import pandas as pd
import csv

class Users:
    def __init__(self, a):
        self.users_file = './users/users.csv'
        self.writer_lock = a.gen_wlock()

    def add_new_customer(self, customerID, password):
        if self.writer_lock.acquire(blocking=True, timeout=5):
            try:
                df_users = pd.read_csv(self.users_file)
                # get the id column
                df_users = df_users.loc[df_users['userID'] == customerID]

                # if no matches found
                if df_users.empty:
                    with open("./users/users.csv", "a", newline="") as users_csv:
                        orders_writer = csv.writer(users_csv, delimiter=',')
                        orders_writer.writerow([customerID, password])
                    return "User successfully added"
                # otherwise username already present
                else:
                    return "User already exists"
            finally:
                writer_lock.release()