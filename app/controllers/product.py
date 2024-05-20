from app.services.productservice import ProductService


class products_controller:
    def get_products(self):
         #instantiate the product service
        data = ProductService()
        return data.get_products()
    


