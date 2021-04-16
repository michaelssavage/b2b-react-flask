import csv
import pandas as pd

class LoginHandler:
    def __init__(self, a):
        self.file = "./users/users.csv"
        self.a = a

    def signUp(self, name, password):
        if self.alreadyExists(name):
            # print("That username already exists")
            return False
        else:
            fieldnames = ['name', 'password']
            b = self.a.gen_wlock()
            if b.acquire(blocking=True, timeout=5):
                try:
                    with open(self.file,  mode='a+', encoding="utf-8", newline='') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow({"name": name, "password": password})
                        # print("signup created")
                        return True
                finally:
                    b.release()

    def alreadyExists(self, name):
        status = False
        b = self.a.gen_rlock()
        if b.acquire(blocking=True, timeout=5):
            try:
                df = pd.read_csv(self.file)
                df = df.loc[df['userID'] == name]

                if df.empty:
                    status = False
                else:
                    status = True
            finally:
                b.release()
                
            return status


    def checkLogin(self, name, password):
        status = False
        b = self.a.gen_rlock()
        if b.acquire(blocking=True, timeout=5):
            try:
                df = pd.read_csv(self.file)
                df = df.loc[(df['userID'] == name) & (df['password'] == password)]

                if df.empty:
                    status = False
                else:
                    status = True
            finally:
                b.release()

            return status