from flask import json
from config import Config

class shoppingcart:
     
    def __init__(self, config):
        """Initialize an empty shopping cart."""
        self.items = []
        self.config = config


    def cart_empty(self):
        """Check if the cart array is empty"""
        if len(self.items) == 0:
            return True
        else:
            return False



    def add_product(self, product_name, quantity, price, image):
        """Add a product to the shopping cart with a specified quantity."""
        self.items.append({"product": product_name, "quantity": quantity, "price":price, "image" : image})
        
        # Serialize and write the updated cart items to cart.json
        with open(self.config['WRITE_TO_CART'], 'w') as cart_file:
            json.dump(self.items, cart_file)

    def remove_product(self, product):
        """Remove a product from the shopping cart."""
        for item in self.items:
            if item["product"] == product:
                self.items.remove(item)
                return True  # Item removed
            else:
                print ("item not in the cart. Please add it first")
        

    def calculate_total(self):
        """Calculate the total cost of all items in the shopping cart."""
        total = 0
        for item in self.items:
            total = total + item["price"] * item["quantity"]
        return total
