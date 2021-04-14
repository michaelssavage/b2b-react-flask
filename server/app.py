from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
import csv

from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

# Custom packages
import users
from orders import Order
import products
import datetime
import pandas as pd

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}

app = Flask(__name__)
auth = HTTPBasicAuth()
cors = CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def index():
    return jsonify("Hello, {}!".format(auth.current_user()))


@app.route("/api/products", methods=["GET"])
def home():
    # read products file
    if (request.method == 'GET'):
        with open('./products/products.json', "r") as json_file:
            data = json.load(json_file)
    
    return jsonify(data)


# Login as a specific customer ID
@app.route("/api/login", methods=["POST"])
def login():
    if (request.method == 'POST'):
        data = request.get_json()

    return jsonify("Howdy ", data)


# Provide a list of projected product availability over the next 6 months (given restocks and current orders).
@app.route("/api/availability_future", methods=["GET"])
def check_availability_future():
    if (request.method == 'GET'):
        # some sort of chart may be useful here
        return jsonify("Plenty of stuff sir")


# Check the available quantity of a product given a specified day and time.
@app.route("/api/availability_check", methods=["GET"])
def check_availability():
    if (request.method == 'GET'):
        # need to parse quantity and product from json body
        return jsonify("Some weather hi")


# Place order
@app.route("/api/order", methods=["POST"])
def place_order():
    if (request.method == 'POST'):
        # parse order details
        data = request.get_json()

        customer_id = data['customer_id']
        product = data['product_name']
        quantity = data['quantity']
        day = data['day']
        month = data['month']

        order_date = datetime.datetime(datetime.datetime.now().year, month, day)
        
        cust_order = Order.Order(customer_id, product, order_date.strftime("%d/%m/%Y"), quantity)
        
        result = Order.placeOrder(cust_order)
        return jsonify(result)

    else:
        return jsonify("Error, POST requests only please")

# https://datatofish.com/export-pandas-dataframe-json/
@app.route("/api/check_orders", methods=["POST"])
def check_orders():
    if (request.method == 'POST'):
        # parse and return order file
        data = request.get_json()
        customer_id = data['customer_id']

        Order.getUserOrders(customer_id)


    else:
        return jsonify("Error, POST requests only please")
    

@app.route("/api/delete_order", methods=["POST"])
def delete_order():
    if (request.method == 'POST'):
        # parse and return order file
        data = request.get_json()
        customer_id = data['customer_id']
        order_ID = data['orderID']

        return jsonify(Order.deleteUserOrder(customer_id, order_ID))


@app.route("/api/add_customer", methods=["POST"])
def add_user():
    if (request.method == 'POST'):        
        data = request.get_json()
        customer_id = data['customer_id']
        password = data['password']
        result = add_new_customer(customer_id, password)

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


def add_new_customer(customer_id, password):
    df_users = pd.read_csv('./users/users.csv')
    # get the id column
    df_users = df_users.loc[df_users['userID'] == customer_id]

    # if no matches found
    if df_users.empty:
        with open("./users/users.csv", "a", newline="") as users_csv:
            orders_writer = csv.writer(users_csv, delimiter=',')
            orders_writer.writerow([customer_id, password])
        return "User successfully added"
    # otherwise username already present
    else:
        return "User already exists"


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
