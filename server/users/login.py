import csv

loggedIn = False

while login == False:
    data = []
    with open("login.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    print(data)

    name = 