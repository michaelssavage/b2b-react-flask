from flask import Flask, jsonify, request, json, session, redirect,url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin
from api.loginHandler import LoginHandler

app = Flask(__name__)
app.secret_key = "any random string"
cors = CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})
loginHandler = LoginHandler()

# Routing a call to path "/" to this method (root endpoint)
@app.route("/api", methods=["GET"])
def home():
    return jsonify("Hello and Welcome. This is the home page of our API!")

# Sign In as a specific customer ID
@app.route("/api/login", methods=["POST"])
def login():
    name = request.json['name']
    password = request.json['password']
    loginHandler.checkLogin(name['name'], password['password'])

    session.clear()
    session['username'] = name['name']
    #return a session token or cookie????
    return ""

# Sign In as a specific customer ID
@app.route("/api/signup", methods=["POST"])
def signup():
    name = request.json['name']
    password = request.json['password']
    loginHandler.signUp(name['name'], password['password'])
    return ""

# Provide a list of projected product availability over the next 6 months (given restocks and current orders).
@app.route("/api/availability_future", methods=["GET"])
def availability_future():
    # some sort of chart may be useful here
    return jsonify("Plenty of stuff sir")

# Check the available quantity of a product given a specified day and time.
@app.route("/api/availability_check", methods=["POST"])
def availability_check():
    # need to parse quantity and product from json body
    return jsonify("Some weather hi")

@app.route("/api/order", methods=["POST"])
def order():
    # parse order details
    return jsonify("Order Received")

@app.route("/api/check_orders", methods=["GET"])
def check_orders():
    # parse and return order file
    return jsonify("Order Received")

@app.route("/api/delete_order", methods=["GET"])
def delete_order():
    # might be used from check orders page
    return jsonify("Order Deleted")

# File Not Found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify("The resource could not be found")

# Server Error
@app.errorhandler(500)
def server_error(e):
    return jsonify("ERROR: The HTTP request sent caused a server error")

# HTTP endpoint not implemented
@app.errorhandler(501)
def not_implemented(e):
    return jsonify("ERROR: This URL does not accept the HTTP request sent")


if __name__ == '__main__':
    app.run(threaded=True)