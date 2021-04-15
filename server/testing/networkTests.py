import requests
# import pytest

base_url = 'http://127.0.0.1:5000/api'

def test_login():
    r = requests.post(
        base_url + '/login', 
        json={"kevin": "123456"})
    assert r.status_code == 200

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

def add_new_user():
    r = requests.post(
        base_url + '/add_customer', 
        json={
            "customerID" : "henry", 
            "password": "theHoover"}
        )
    print(r.content)

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


if __name__ == '__main__':
    # test_place_order()
    # add_new_user()
    # get_orders()
    delete_order()
    # get_products()
