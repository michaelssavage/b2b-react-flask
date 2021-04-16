from orders.Order import Order
from orders.Order import placeOrder, deleteUserOrder, getUserOrders
from products.Product import getFutureAvailability
from users.loginHandler import LoginHandler
import datetime

def localPlaceOrder():
    order_date = datetime.datetime(datetime.datetime.now().year, 3, 1)
    print(placeOrder(Order("user43", "jolt cola", order_date.strftime("%d/%m/%Y"), 200)))

def localDeleteOrder():
    print(deleteUserOrder("user43", 97))

def localGetOrder():
    print(getUserOrders("user4"))

def localGetFutureAvailability():
    print(getFutureAvailability("oranges", 1))

def localCheckLogin():
    login = LoginHandler()
    print(login.signUp("gerard", "jo"))
    print(login.checkLogin("test","pass"))
