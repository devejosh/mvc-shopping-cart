#Import default flask modules for user in the file. 
from flask import render_template, request, url_for, redirect
import traceback


#import helper 
from utils import helper
helper = helper()

#import exception handler 
from app.controllers.exceptions import exceptions
#instantiate the exception handler
checkforexceptions = exceptions()

#Import the shopping cart module to interact with the database
from app.models.models import shoppingcart
#Instanciate the shopping cart model
cart = shoppingcart()

#Import the config file to get absolute path information
from config import Config
#Instantiate the config object
config = Config()




class CartServices:
    
    def check_cart():
        try:
            #check if my_cart is empty. 
            if cart.cart_empty() == True:
                return render_template(config.EMPTY_CART)
            
            #If not, get the data in the cart and display in the cart.html page. 
            else:
                    cartdata = cart.items
                    total = cart.calculate_total() 
                    return render_template('cart.html', data=cartdata,  finalttl = total)
        except:
                traceback.print_exc()
                return render_template(config.ERROR_404)
        
    def additems():
         try:
              if request.method not in ['GET', 'POST']:
                return render_template(config.ERROR_404)
              
              else:
                
                if (request.method == 'POST'):
                    #Check data for exceptions
                    error = checkforexceptions.checkdata(request.form.get('product_name'), request.form.get('price'), request.form.get('quantity'), request.form.get('product_image'))

                    #If the exception handler finds an error, return the error message. 
                    if error:
                        return render_template(config.ERROR_404, error=error)
                    else:
                        #If no error, add the item to the cart. 
                        #Make sure that the quantity and price are variables and not strings. 
                        
                        quantity = helper.safe_int(request.form.get('quantity'))
                        price = helper.safe_int(request.form.get('price'))
                        
                        cart.add_to_cart(request.form.get('product_name'), price, quantity, request.form.get('product_image'))

                        #Return to the cart page
                        CartServices.check_cart()
                        
                
                else:
                     return render_template(config.ERROR_404)
         except:
            traceback.print_exc()
            return render_template(config.ERROR_404)
         

    def remove_from_cart():
        if request.method == 'POST':
            try:
                product = request.form.get('product')
                cart.remove_product(product)
            except Exception as e:
                print(f"Error removing product from the cart : {str(e)}")
                return redirect(url_for('cart'))
