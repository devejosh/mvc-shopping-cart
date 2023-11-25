#default imports
from flask import Flask, render_template, request, redirect, url_for, json

#custom imports
from config import Config
from utils import helper
from app.models.models import shoppingcart

app = Flask(__name__)
app.config.from_object(Config)


# Instantiate an empty shopping cart at the start
my_cart = shoppingcart(app.config)
helper_methods = helper()

# Custom error page for 404 (page not found errors)
@app.errorhandler(404)
def pagenotfound(error):
    return render_template(app.config['ERROR_404']), 404


@app.route('/')
def home():
    try:
        with open(app.config['PRODUCTS_FILE'], 'r') as products:
            data = json.load(products)
        return render_template('index.html', data=data)
    except FileNotFoundError:
        return render_template('404.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/cart')
def cart():  
        #check if my_cart is empty. 
        if my_cart.cart_empty() == True:
            return render_template(app.config['EMPTY_CART'])
        else:
                cartdata = my_cart.items
                total = my_cart.calculate_total() 
                return render_template('cart.html', data=cartdata,  finalttl = total)
        


@app.route('/addtocart', methods=['GET', 'POST'])
def addtocart():
    if request.method == 'POST':
        # Process the POST request data
        product_name = request.form.get('product')
       
        price = helper_methods.safe_float(request.form.get('price'))
        quantity = helper_methods.safe_int(request.form.get('quantity'))
        image = request.form.get('image')

        if price is not None and quantity is not None:
            my_cart.add_product(product_name, quantity, price, image)
    return redirect(url_for('home'))



@app.route('/remove-from-cart', methods=['POST'])
def removefromcart():
    if request.method == 'POST':
        #process the request and remove the data from the cart array based on the prduct name
        try:
            product = request.form.get('product')
            my_cart.remove_product(product)
        except Exception as e:
            print(f"Error removing product from the cart : {str(e)}")
    return redirect(url_for('cart'))



if __name__ == '__main__':
    app.run(debug=True)
