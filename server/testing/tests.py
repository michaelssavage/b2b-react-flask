import requests
# import pytest

def test_login():
    r = requests.post('http://127.0.0.1:5000/login', json={"kevin": "123456"})
    assert r.status_code == 200

def test_place_order():
    r = requests.post('http://127.0.0.1:5000/order', json={"customer_id" : "user42", "product_name": "game boy", "quantity" : 2, "day": 14, "month": 2})
    print(r.status_code)

def get_orders():
    pass

if __name__ == '__main__':
    test_place_order()