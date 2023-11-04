from flask import Flask
from flask import render_template
from flask import jsonify, json


app = Flask(__name__)


@app.route('/')
def home():
    try:
        with open('data/products.json', 'r') as products:
            data = json.load(products)
        return render_template('index.html', data=data)
    except FileNotFoundError :
        return render_template('404.html')
    


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/cart')
def cart():

    return render_template('cart.html')




if __name__ == '__main__':
    app.run(debug=True)
