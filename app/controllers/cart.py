import traceback
from app.services.cartservice import CartServices


class cart_controller:

    try:
        def view_cart(self):
            cart = CartServices()
            return cart.check_cart()
           
    
        def additemtocart(self):
            cart = CartServices()
            return cart.additems()
            
    
        def remove_from_cart(self):
            cart = CartServices()
            return cart.remove_from_cart()
    
    except:
        print("An error occurred:")
        traceback.print_exc()


 