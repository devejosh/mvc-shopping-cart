from flask import Flask, render_template, request, redirect, url_for, json
from app.models.models import shoppingcart

app = Flask(__name__)

# Instantiate an empty shopping cart at
my_cart = shoppingcart()

# Custom error page for 404 (page not found errors)


@app.errorhandler(404)
def pagenotfound(error):
    return render_template('components/404.html'), 404


@app.route('/')
def home():
    try:
        with open('data/products.json', 'r') as products:
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
            return render_template('components/emptycart.html')
        else:
                cartdata = my_cart.items
                total = my_cart.calculate_total() 
                return render_template('cart.html', data=cartdata,  finalttl = total)
        



@app.route('/addtocart', methods=['GET', 'POST'])
def addtocart():
    if request.method == 'POST':
        # Process the POST request data
        product_name = request.form.get('product')
        price = safe_float(request.form.get('price'))
        quantity = safe_int(request.form.get('quantity'))
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
        except:
            print("error in logic")
    
    return redirect(url_for('cart'))

# Helper methods
def safe_float(value):
    try:
        # Remove commas and convert to float
        return float(value.replace(',', ''))
    except ValueError:
        # Handle invalid float values
        return None


def safe_int(value):
    try:
        # Remove commas and convert to integer
        return int(value.replace(',', ''))
    except ValueError:
        # Handle invalid integer values
        return None



if __name__ == '__main__':
    app.run(debug=True)
