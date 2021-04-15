import csv

class LoginHandler:

    def __init__(self):
        self.file = "users.csv"

    def signUp(self, name, password):
        fieldnames = ['name', 'password']
        with open(self.file,  mode='a+', encoding="utf-8", newline='') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if self.alreadyExists(name):
                print("That username already exists")
            else:
                writer.writerow({"name": name, "password": password})
                print("signup created")
        return None

    def alreadyExists(self, name):
        exists = False
        with open(self.file, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['userID'] == name:
                    exists = True
                    return exists
            return exists

    def checkLogin(self, name, password):
        valid = False
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

if __name__ == '__main__':
    login = LoginHandler()
    #login.signUp("gerard", "jo")
    login.checkLogin("john","jof")
