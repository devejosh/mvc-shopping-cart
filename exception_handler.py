#Imports 
from utils import helper

#Instantiation 
helper_methods = helper()

class exceptions:
    def checkdata(self, product_name, price, quantity, product_image):
        # Check that all variables have a value in them.
        if not all((product_name, price, quantity, product_image)):
            return "The form data is missing some values. Please refresh the page and try adding the product to the cart again"
        else:
            if (helper_methods.safe_int(quantity) <= 0):
                return "You've entered an invalid quantity. Values of 1 and above will be supported."
            
