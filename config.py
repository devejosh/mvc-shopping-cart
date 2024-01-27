import os

#using absolute paths to address issues with file access
class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    #Paths
    PRODUCTS_FILE = os.path.join(BASE_DIR, 'data/products.json')
    WRITE_TO_CART = os.path.join(BASE_DIR, 'data/cart.json')
    EMPTY_CART = 'components/emptycart.html'
    ERROR_404 = 'components/404.html'

    #FORM
    FORM_ERROR = 'components/error handler/error.html'

    #Input sanitization when the form is processed.
    INVALID_INPUT = 'components/error handler/error.html'
    
