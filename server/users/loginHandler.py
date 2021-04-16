import csv

class LoginHandler:
    def __init__(self, a):
        self.file = "./users/users.csv"
        self.reader_lock = a.gen_rlock()
        self.writer_lock = a.gen_wlock()

    def signUp(self, name, password):
        success = True
        fieldnames = ['name', 'password']

        if self.writer_lock.acquire(blocking=True, timeout=5):
            try:
                with open(self.file,  mode='a+', encoding="utf-8", newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    if self.alreadyExists(name):
                        print("That username already exists")
                        success = False
                    else:
                        writer.writerow({"name": name, "password": password})
                        print("signup created")
                return success
            finally:
                self.writer_lock.release()

    def alreadyExists(self, name):
        exists = False
        if self.reader_lock.acquire(blocking=True, timeout=5):
            try:
                with open(self.file, mode='r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['userID'] == name:
                            exists = True
                            return exists
                    return exists
            finally:
                self.reader_lock.release()


    def checkLogin(self, name, password):
        valid = False
        if self.reader_lock.acquire(blocking=True, timeout=5):
            try:
                with open(self.file, mode='r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)

                    for row in reader:
                        if row['userID'] == name and row['password'] == password:
                            valid = True
                        
                    if valid:
                        print("valid login")
                    else:
                        print("invalid login")
                    return valid
            finally:
                self.reader_lock.release()

if __name__ == '__main__':
    login = LoginHandler()
    #login.signUp("gerard", "jo")
    login.checkLogin("test","pass")
