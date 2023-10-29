class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def remove_product(self, product):
        for item in self.items:
            if item["product"] == product:
                self.items.remove(item)
                return True  # Item removed
        return False  # Item not found in the cart

    def calculate_total(self):
        total = 0
        for item in self.items:
            total = total + item["product"].price * item["quantity"]
            return total



