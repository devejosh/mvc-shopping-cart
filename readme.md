# Flask Shopping Cart Application

This project is a simple e-commerce website built with Flask, featuring product listings, a shopping cart, and a contact page. Users can browse products, add them to the cart, and contact the site admin. The application is designed to provide a basic yet functional online shopping experience.

## Table of Contents

- [Current Features](#current-features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Planned Improvements](#planned-improvements)
- [Contributing](#contributing)

## Current Features

- **Product Listings**: Display a list of products with details and prices.
- **Shopping Cart**: Users can add products to a shopping cart and view the cart.
- **Contact Page**: A simple form allowing users to send messages to the administrator.
- **Error Handling**: Custom error pages for 404 and 500 status codes.

## Technologies Used

- **Python**: The core backend language.
- **Flask**: A lightweight WSGI web application framework.
- **HTML/CSS**: For structuring and styling the frontend.
- **JavaScript**: Minimal usage for enhancing frontend interactions.

## Setup and Installation


1. **Clone the repository:**
 git clone https://github.com/devejosh/mvc-shopping-cart.git

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```


6. **Run the application:**
   ```bash
   python main.py
   ```

5. **Navigate to** `http://127.0.0.1:5000/` **in your browser.**

## Planned Improvements

- **User Authentication**: Implement user login functionality to manage sessions and personalize shopping carts.
- **Input Validation and Sanitization**: Enhance security by validating and sanitizing inputs using Flask-WTF and Bleach.
- **Concurrency Handling**: Address concurrency issues using database transactions or Redis to ensure data consistency.
- **Enhanced Logging**: Implement structured logging with log rotation to facilitate better monitoring and debugging.
- **Unit Testing**: Develop comprehensive unit tests for all critical functionalities to ensure reliability.
- **Session Management**: Improve session management using server-side storage for enhanced security.
- **Code Documentation**: Document all functions and classes thoroughly to improve maintainability.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

Please ensure to update tests as appropriate and adhere to the existing coding style.

---

Thank you for your interest in our Flask shopping cart project! We look forward to your contributions and hope you find this project useful for your learning and development.