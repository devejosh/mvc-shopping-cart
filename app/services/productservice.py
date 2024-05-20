#Import the json module
import json

#Import the render_template module
from flask import render_template

# Import the config file to get absolute path information
from config import Config


class ProductService:

    def __init__(self):
        self.config = Config()

    def get_products(self):
        try:
            with open(self.config.PRODUCTS_FILE, 'r') as products:
                data = json.load(products)
            return render_template('index.html', data=data)
        except FileNotFoundError:
            return render_template(self.config.ERROR_404)
        
   