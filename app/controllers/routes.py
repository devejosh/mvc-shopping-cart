#import the render template module  
from flask import render_template\

#import the config file
from config import Config
config_data = Config()


class route_controller:  
    def contact():
        try : 
            return render_template('contact.html')
        except FileNotFoundError:
            return render_template(config_data.ERROR_404)
