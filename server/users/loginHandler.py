import csv
import pandas as pd

class LoginHandler:
    def __init__(self, a):
        self.file = "./users/users.csv"
        self.reader_lock = a.gen_rlock()
        self.writer_lock = a.gen_wlock()

    def signUp(self, name, password):
        if self.alreadyExists(name):
            # print("That username already exists")
            return False
        else:
            fieldnames = ['name', 'password']
            if self.writer_lock.acquire(blocking=True, timeout=5):
                try:
                    with open(self.file,  mode='a+', encoding="utf-8", newline='') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow({"name": name, "password": password})
                        # print("signup created")
                        return True
                finally:
                    self.writer_lock.release()

    def alreadyExists(self, name):
        if self.reader_lock.acquire(blocking=True, timeout=5):
            try:
                df = pd.read_csv(self.file)
                df = df.loc[df['userID'] == name]

                if df.empty:
                    return False
                else:
                    return True
            finally:
                self.reader_lock.release()


    def checkLogin(self, name, password):
        if self.reader_lock.acquire(blocking=True, timeout=5):
            try:
                df = pd.read_csv(self.file)
                df = df.loc[(df['userID'] == name) & (df['password'] == password)]

                if df.empty:
                    return False
                else:
                    return True
            finally:
                self.reader_lock.release()