#default imports
from flask import Flask, render_template, request
import logging


#Importing all controllers
from app.controllers.product import products_controller
from app.controllers.routes import route_controller
from app.controllers.cart import cart_controller


app = Flask(__name__)


# Setup logging
logging.basicConfig(filename='error.log', level=logging.ERROR)


@app.route('/')
def home():
    data = products_controller()
    return data.get_products()
    


@app.route('/contact')
def contact():
    route = route_controller()
    return route.contact()


@app.route('/cart')
def cart(): 
    cart = cart_controller()
    return cart.view_cart()


@app.route('/add-to-cart' , methods=['POST'])
def addtocart():
        cart = cart_controller()
        return cart.additemtocart()


@app.route('/remove-from-cart', methods=['POST'])
def removefromcart():
     cart = cart_controller()
     return cart.remove_from_cart()
    


if __name__ == '__main__':
    app.run(debug=True)
