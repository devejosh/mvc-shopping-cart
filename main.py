from flask import Flask, render_template, request, redirect, url_for, json
from app.models import shoppingcart

app = Flask(__name__)

# Instantiate an empty shopping cart at 
cart = shoppingcart()

#Custom error page for 404 (page not found errors)

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
    return render_template('cart.html')



@app.route('/addtocart')
def addtocart():
   
    product_name = request.form.get('product')
    price = float(request.form.get('price'))
    quantity = int(request.form.get('quantity'))
    image = request.form.get('image')
    cart.add_product(product_name, quantity, price,image)
    
    return redirect(url_for('index'))

 
if __name__ == '__main__':
    app.run(debug=True)
