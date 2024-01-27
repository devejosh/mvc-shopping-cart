#Imports 
from utils import helper

#Instantiation 
helper_methods = helper()

class exceptions:
    def checkdata(self, product_name, price, quantity, product_image):
        # Check that all variables have a value in them.
        if not all((product_name, price, quantity, product_image)):
            return "The form data is missing some values. Please refresh the page and try adding the product to the cart again", None, None

        try:
            price = helper_methods.safe_int(price)
            quantity = helper_methods.safe_int(quantity)
            
            if price <= 0 or quantity <= 0:
                return "Issue with the price or quantity of the product. Both price and quantity should be positive numbers.", type(price).__name__, type(quantity).__name__
            else:
                return None, type(price).__name__, type(quantity).__name__

        except ValueError as e:
            return f"Invalid price or quantity. Please enter valid numerical values. Details: {str(e)}", None, None
