import requests
# import pytest

def test_login():
    r = requests.post('http://127.0.0.1:5000/api/login', json={"kevin": "123456"})
    assert r.status_code == 200

def test_place_order():
    r = requests.post('http://127.0.0.1:5000/api/order', json={"customer_id" : "user4", "product_name": "playstation5", "quantity" : 2, "day": 14, "month": 2})
    print(r.content)
    print(r.status_code)

def get_orders():
    r = requests.post('http://127.0.0.1:5000/api/check_orders', json={"customer_id" : "user4"})
    print(r.content)
    print(r.status_code)

def add_new_user():
    r = requests.post('http://127.0.0.1:5000/api/add_customer', json={"customer_id" : "test1", "password": "pass"})
    print(r.content)

def delete_order():
    r = requests.post('http://127.0.0.1:5000/api/delete_order', json={"customer_id" : "user43", "orderID": 97})
    print(r.content)


if __name__ == '__main__':
    # test_place_order()
    # add_new_user()
    # get_orders()
    delete_order()