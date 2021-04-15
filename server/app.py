from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin

import json
import csv
import threading
import datetime
import pandas as pd

lock = threading.Lock()

# Custom packages
from orders import Order
from users import User
from products import Product
from users import Users

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})


@app.route("/api/products", methods=["GET"])
def home():
    # read products file
    if (request.method == 'GET'):
        return Product.getproducts()
    else:
        return make_response()


# Provide a list of projected product availability over the next 6 months (given restocks and current orders).
@app.route("/api/availability_future", methods=["POST"])
def check_availability_future():
    if (request.method == 'POST'):
        data = request.get_json()
        product = data['product']
        timePeriod = data['date']
        result = Product.getFutureAvailability(
                    product, 
                    int(timePeriod)
                )
        return jsonify(result)


# Check the available quantity of a product given a specified day and time.
@app.route("/api/availability_check", methods=["GET"])
def check_availability():                                                           # TODO
    if (request.method == 'GET'):
        # need to parse quantity and product from json body
        return jsonify("Some weather hi")


# Place order
@app.route("/api/order", methods=["POST"])
def place_order():
    if (request.method == 'POST'):
        # parse order details
        data = request.get_json()

        customerID = data['customerID']
        product = data['product_name']
        quantity = int(data['quantity'])
        day = int(data['day'])
        month = int(data['month'])

        order_date = datetime.datetime(datetime.datetime.now().year, month, day)
        
        cust_order = Order.Order(customerID, product, order_date.strftime("%d/%m/%Y"), quantity)
        
        result = Order.placeOrder(cust_order)
        return jsonify(result)


@app.route("/api/check_orders", methods=["POST"])
def check_orders():
    if (request.method == 'POST'):
        # parse and return order file
        data = request.get_json()
        customerID = data['customerID']
        return Order.getUserOrders(customerID)
    

@app.route("/api/delete_order", methods=["POST"])
def delete_order():
    if (request.method == 'POST'):
        # parse and return order file
        data = request.get_json()
        customerID = data['customerID']
        order_ID = data['orderID']
        # print(customerID, order_ID)        
        return jsonify(Order.deleteUserOrder(customerID, order_ID))


@app.route("/api/add_customer", methods=["POST"])
def add_user():
    if (request.method == 'POST'):        
        data = request.get_json()
        customerID = data['customerID']
        password = data['password']
        result = Users.add_new_customer(customerID, password)
        return jsonify(result)


#################################################
############ Error Handling #####################
#################################################
# File Not Found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify("ERROR: The resource could not be found")

# Server Error
@app.errorhandler(500)
def server_error(e):
    return jsonify("ERROR: The HTTP request sent caused a server error")

# HTTP endpoint not implemented
@app.errorhandler(501)
def not_implemented(e):
    return jsonify("ERROR: This URL does not accept the HTTP request sent")


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
