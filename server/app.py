from flask import Flask, jsonify, request
import json
import csv

# Custom packages
import users
from orders import Order
import products
import datetime

# from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# login stuff, needs to be implemented
# login_manager = LoginManager()
# login_manager.init_app(app)

# Routing a call to path "/" to this method (root endpoint)
@app.route("/", methods=["GET"])
def home():
    # read products file
    if (request.method == 'GET'):
        with open('./products/products.json', "r") as json_file:
            data = json.load(json_file)
    
    return jsonify(data)


# Login as a specific customer ID
@app.route("/login", methods=["POST"])
def login():
    if (request.method == 'POST'):
        data = request.get_json()

    return jsonify("Howdy ", data)


# Provide a list of projected product availability over the next 6 months (given restocks and current orders).
@app.route("/availability_future", methods=["GET"])
def check_availability_future():
    if (request.method == 'GET'):
        # some sort of chart may be useful here
        return jsonify("Plenty of stuff sir")


# Check the available quantity of a product given a specified day and time.
@app.route("/availability_check", methods=["GET"])
def check_availability():
    if (request.method == 'GET'):
        # need to parse quantity and product from json body
        return jsonify("Some weather hi")


# Place order
@app.route("/order", methods=["POST"])
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
        
        # store in file
        with open("./orders/orders.json", "a") as orders_file:
            # find user in file
            # TODO
            json.dump(cust_order.toJSON(), orders_file, indent=4)

    else:
        return jsonify("Error, POST requests only please")
    
    return jsonify("Order Received, Thank you")


@app.route("/check_orders", methods=["POST"])
def check_orders():
    if (request.method == 'POST'):
        # parse and return order file
        data = request.get_json()
        customer_id = data['customer_id']

        return jsonify(get_orders(customer_id))

    else:
        return jsonify("Error, POST requests only please")
    

@app.route("/delete_order", methods=["POST"])
def delete_order():
    if (request.method == 'POST'):
        # parse delete request
        data = request.get_json()

    # might be used from check orders page
    return jsonify("Order Deleted")

@app.route("/add_customer", methods=["POST"])
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
    return jsonify("ERRPR: The resource could not be found")

# Server Error
@app.errorhandler(500)
def server_error(e):
    return jsonify("ERROR: The HTTP request sent caused a server error")

# HTTP endpoint not implemented
@app.errorhandler(501)
def not_implemented(e):
    return jsonify("ERROR: This URL does not accept the HTTP request sent")



# TODO: need to change this to get the id of a logged in user
def get_orders(customer_id):
    with open("./orders/orders.json", "r") as json_file:
        try:
            data = json.load(json_file)
            return data[customer_id]
        except:
            return "No orders for this user"


def add_new_customer(customer_id, password):
    # TODO check if user already exists
    # if customer_id not in csv_file:
    with open('./users/users.csv', 'a+', newline='') as users_file:
        data = csv.DictReader(users_file)
        for row in data:
            if row['userID'] == customer_id:
                return "User already exists"

            else:
                csv_writer = csv.writer(users_file)
                csv_writer.writerow([customer_id, password])
                return "Users successfully added"


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
