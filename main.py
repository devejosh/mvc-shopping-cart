#default imports
from flask import Flask, render_template, request, redirect, url_for, json
import traceback

#custom imports
from config import Config
from exception_handler import exceptions
from app.models.models import shoppingcart
from utils import helper

app = Flask(__name__)
app.config.from_object(Config)


# Instantiate an empty shopping cart at the start
my_cart = shoppingcart(app.config)
checkexceptions = exceptions()



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
        return render_template(app.config('ERROR_404'))


@app.route('/contact')
def contact():
    try:
        return render_template('contact.html')
    except:
        return render_template("404.html")



@app.route('/cart')
def cart(): 
        try:
            #check if my_cart is empty. 
            if my_cart.cart_empty() == True:
                return render_template(app.config['EMPTY_CART'])
            else:
                    cartdata = my_cart.items
                    total = my_cart.calculate_total() 
                    return render_template('cart.html', data=cartdata,  finalttl = total)
        except:
                traceback.print_exc()
                return render_template(app.config['ERROR_404'])
        


@app.route('/addtocart', methods=['GET', 'POST'])
def addtocart():
        try:  
            if request.method == 'POST':
                
                #Check data for exceptions
                error = checkexceptions.checkdata(request.form.get('product_name'), request.form.get('price'), request.form.get('quantity'), request.form.get('product_image'))
              
              
              # check if the checkdata method retuned an error
                if error:
                   return render_template(app.config['INVALID_INPUT'], data=error)
                
                else:
                    if error is None:
                        print("We are adding some data to the cart now")
                        #Store data from the form in variables
                        product_name = request.form.get('product_name')
                        price = request.form.get('price')
                        quantity = request.form.get('quantity')
                        product_image = request.form.get('product_image')
                        print ("calling the cart function")
                        
                        #Call the add product method from the shopping cart class to add the product to cart.
                        #Instaciate the helper class to make sure quanitity and price are integers and not strings. This helps when doing calculations. 
                        
                        helper_instance = helper()
                        quantity = helper_instance.safe_int(quantity)
                        price = helper_instance.safe_int(price)

                        my_cart.add_product(product_name, quantity, price, product_image)

                        #retuning to the index page after adding items to cart
                        print ("Item added to the cart, returning to the index page")
                        return redirect(url_for('home'))
            else:
                 print("Issue with the code. We are checking.")
        except:
             return render_template(app.config['ERROR_404'], data=traceback.print_exc())


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
