# Simple E-Commerce Website with Shopping Cart

This is a simple e-commerce website built with Flask that features product listings, a shopping cart, and a contact page. Users can browse products, add them to the cart, and contact the site admin.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Deployment](#deployment)

## Introduction

This Flask-based e-commerce website provides the following functionality:

- Display a list of products with details and prices.
- Add products to a shopping cart.
- View the shopping cart with a list of added products.
- Contact the admin using a simple contact form.
- A responsive design for mobile and desktop users.
- Basic CSS animations for product tiles and buttons.

## Prerequisites

Before running this project, make sure you have the following prerequisites:

- Python 3.6+
- Flask (can be installed via `pip`)

```bash
pip install Flask
```

## Project structure

mvc-shopping-cart/
   ├── app.py
   ├── templates/
   │   ├── index.html
   │   ├── cart.html
   │   └── product.html
   ├── static/
   │   ├── components/
   │   │   ├── header.html
   │   │   └── footer.html
   │   ├── css/
   │   │   └── style.css
   │   ├── images/
   │   │   └── (product images)
   │   └── js/
   │       └── script.js
   ├── data/
   │   ├── products.json
   └── venv/ (Your virtual environment)
