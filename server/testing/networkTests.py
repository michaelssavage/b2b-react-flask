import threading
import requests
import time
import random

base_url = 'http://127.0.0.1:5000/api'

users = ["john", "mary", "columbus", "gerard", "michael", "jospeh", "brendan", "patrick", "andrew", "david"]
passwords = ["pass", "password", "betterPassword", "password1", "passwordsRule", "iforgotmypassword", "mydogryan", "ca4006", "DCU", "case4"]




def test_place_order():
    r = requests.post(
        base_url + '/order', 
        json={
            "customerID" : "user4", 
            "product_name": "oranges", 
            "quantity" : 2, 
            "day": 14, 
            "month": 2
            }
        )
    print(r.content)
    print(r.status_code)


def get_orders():
    r = requests.post(
        base_url + '/check_orders', 
        json={"customerID" : "user4"}
        )
    print(r.content)
    print(r.status_code)


def delete_order():
    r = requests.post(
        base_url + '/delete_order', 
        json={
            "customerID" : "gerard", 
            "orderID": 10
            }
        )
    print(r.content)


def get_products():
    r = requests.get(
        base_url + '/products'
        )
    print(r.content)


def add_new_user(user, password):
    r = requests.post(
        base_url + '/signup', 
        json={
            "customerID" : user, 
            "password": password}
        )
    assert r.status_code == 201


def test_login(username, password):
    r = requests.post(
        base_url + '/login', 
        json={
            'name': username,
            'password': password
            }
        )
    assert r.status_code == 200


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

def multiUserLogin():
    jobs = []
    for i in range(10):
        t = threading.Thread(target=test_login, args=(users[i], passwords[i]))
        jobs.append(t)

    for j in jobs:
        # random start times
        time.sleep(random.randint(1,5))
        j.start()

    for j in jobs:
        j.join()

    print("Log ins complete")


if __name__ == '__main__':
    multiUserLogin()
