from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin

import datetime
from readerwriterlock import rwlock

# LOCKS
# a fair priority lock
lock = rwlock.RWLockFair()

# Custom packages
from orders.Order import Order, placeOrder, getUserOrders, deleteUserOrder
from products.Product import getFutureAvailability, getProducts
from users import loginHandler

app = Flask(__name__)
loginHandler = loginHandler.LoginHandler(lock)

cors = CORS(
    app, 
    supports_credentials=True, 
    resources={
        r"/api/*": {
            "origins": "*", 
            "allow_headers": "*", 
            "expose_headers": "*"
            }
        }
    )

@app.route('/api/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        customerID = data['name']
        password = data['password']

        if loginHandler.checkLogin(customerID, password):
            # success
            return make_response("Success", 201)
        else:
            # unauthorised
            return make_response("Username Or Password Is Incorrect", 401)

@app.route('/api/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        customerID = data['name']
        password = data['password']

        if loginHandler.signUp(customerID, password):
            # success
            return make_response("Success", 201)
        else:
            # unauthorised
            return make_response("This User Already Exists", 401)

@app.route("/api/products", methods=["GET"])
def home():
    # read products file
    if (request.method == 'GET'):
        return getProducts(lock)

# Provide a list of projected product availability over the next 6 months (given restocks and current orders).
@app.route("/api/availability_future", methods=["POST"])
def check_availability_future():
    if (request.method == 'POST'):
        data = request.get_json()
        product = data['product']
        timePeriod = data['date']
        result = getFutureAvailability(
                    lock,
                    product, 
                    int(timePeriod)
                )
        return jsonify(result)

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
        cust_order = Order(lock, customerID, product, order_date.strftime("%d/%m/%Y"), quantity)
        return placeOrder(lock, cust_order)

@app.route("/api/check_orders", methods=["POST"])
def check_orders():
    if (request.method == 'POST'):
        # parse and return order file
        data = request.get_json()
        customerID = data['customerID']
        return getUserOrders(lock, customerID)

@app.route("/api/delete_order", methods=["POST"])
def delete_order():
    if (request.method == 'POST'):
        # parse and return order file
        data = request.get_json()
        customerID = data['customerID']
        order_ID = data['orderID']
        # print(customerID, order_ID)        
        return deleteUserOrder(lock, customerID, order_ID)


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
