import requests
# import pytest

def test_login():
    r = requests.post('http://127.0.0.1:5000/login', json={"kevin": "123456"})
    assert r.status_code == 200

def test_place_order():
    r = requests.post('http://127.0.0.1:5000/order', json={"customer_id" : "user42", "product_name": "game boy", "quantity" : 2, "day": 14, "month": 2})
    print(r.status_code)

def get_orders():
    r = requests.post('http://127.0.0.1:5000/check_orders', json={"customer_id" : "user4"})
    print(r.content)
    print(r.status_code)

def add_new_user():
    r = requests.post('http://127.0.0.1:5000/add_customer', json={"customer_id" : "test1", "password": "pass"})
    print(r.content)


if __name__ == '__main__':
    test_place_order()
    # add_new_user()
    # get_orders()