class Product:
    def __init__(self, name, price):
        """Initialize a product with a name and price."""
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_product(self, product, quantity):
        """Add a product to the shopping cart with a specified quantity."""
        self.items.append({"product": product, "quantity": quantity})

    def remove_product(self, product):
        """Remove a product from the shopping cart."""
        for item in self.items:
            if item["product"] == product:
                self.items.remove(item)
                return True  # Item removed
        return False  # Item not found in the cart

    def calculate_total(self):
        """Calculate the total cost of all items in the shopping cart."""
        total = 0
        for item in self.items:
            total = total + item["product"].price * item["quantity"]
        return total
