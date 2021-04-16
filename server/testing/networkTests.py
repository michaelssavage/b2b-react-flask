import threading
import requests
import time
import random

base_url = 'http://127.0.0.1:5000/api'

users = ["john", "mary", "columbus", "gerard", "michael", "jospeh", "brendan", "patrick", "andrew", "david"]
passwords = ["pass", "password", "betterPassword", "password1", "passwordsRule", "iforgotmypassword", "mydogryan", "ca4006", "DCU", "case4"]


def delete_order():
    r = requests.post(
        base_url + '/delete_order', 
        json={
            "customerID" : "gerard", 
            "orderID": 10
            }
        )
    print(r.content)


def add_new_user(user, password):
    r = requests.post(
        base_url + '/signup', 
        json={
            "name" : user, 
            "password": password}
        )
    assert r.content != None
    assert r.status_code == 201

def multiUserSignup():
    jobs = []
    for i in range(10):
        t = threading.Thread(target=add_new_user, args=(users[i], passwords[i]))
        jobs.append(t)

    for j in jobs:
        # random start times
        # time.sleep(random.randint(1,5))
        j.start()

    for j in jobs:
        j.join()

    print("Sign ups complete")


def test_login(username, password):
    r = requests.post(
        base_url + '/login', 
        json={
            'name': username,
            'password': password
            }
        )
    assert r.content != None
    assert r.status_code == 201

def multiUserLogin():
    jobs = []
    for i in range(10):
        t = threading.Thread(target=test_login, args=(users[i], passwords[i]))
        jobs.append(t)

    for j in jobs:
        # random start times
        # time.sleep(random.randint(1,5))
        j.start()

    for j in jobs:
        j.join()

    print("Log ins complete")


def get_products():
    r = requests.get(
        base_url + '/products'
        )
    assert r.content != None
    assert r.status_code == 200

def multiUserStockCheck():
    jobs = []
    for _ in range(10):
        t = threading.Thread(target=get_products)
        jobs.append(t)

    for j in jobs:
        # random start times
        # time.sleep(random.randint(1,5))
        j.start()

    for j in jobs:
        j.join()

    print("Stock Checks complete")


def test_place_order(user):
    products = ['Game Boy', 'Apples', 'Oranges', 'Champion Milk', 'Maltesers', 'Fizzy Drinks']
    product = random.choice(products)
    quantity = random.randint(1, 10)
    day = random.randint(1,28)
    month = random.randint(1,12)

    r = requests.post(
        base_url + '/order', 
        json={
            "customerID" : user, 
            "product_name": product, 
            "quantity" : 1, 
            "day": day, 
            "month": month
            }
        )
    assert r.content != None
    assert r.status_code == 200

def multiUserOrder():
    jobs = []
    # 100 orders
    for i in range(100):
        # 10 users
        j = i % 10
        t = threading.Thread(target=test_place_order, args=(users[j],))
        jobs.append(t)

    for j in jobs:
        # random start times
        # time.sleep(random.randint(1,5))
        j.start()

    for j in jobs:
        j.join()

    print("Orders Complete")


def get_orders(user):
    r = requests.post(
        base_url + '/check_orders', 
        json={"customerID" : user}
        )
    assert r.content != None
    assert r.status_code == 200

def multiUserGetOrders():
    jobs = []
    for i in range(10):
        t = threading.Thread(target=get_orders, args=(users[i],))
        jobs.append(t)

    for j in jobs:
        # random start times
        # time.sleep(random.randint(1,5))
        j.start()

    for j in jobs:
        j.join()

    print("Order Checks Complete")

    
if __name__ == '__main__':
    # multiUserGetOrders()
    # multiUserOrder()
    multiUserGetOrders()
