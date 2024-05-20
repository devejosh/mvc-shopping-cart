from flask import Blueprint, render_template 
from app.services.cartservice import CartServices


class cart_controller:

    try:
        def view_cart():
            cart = CartServices()
            response = cart.check_cart()
            return response
    
        def add_to_cart():
            cart = CartServices()
            response = cart.additems()
            return response
    
        def remove_from_cart():
            cart = CartServices()
            response = cart.remove_from_cart()
            return response
    except:

 