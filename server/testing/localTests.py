from Order import placeOrder, deleteUserOrder, getUserOrders
from Product import getFutureAvailability
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
