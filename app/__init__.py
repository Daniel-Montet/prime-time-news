from flask import Flask
#from config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options


"""
initialize application

"""
NEWS_API_KEY = '67b973a2cb15466982de38b10153bfe5'
SECRET_KEY = 'rrrrrraaaaah'
#app= Flask(__name__,instance_relative_config= True)

# Setting up configuration
#app.config.from_object(DevConfig)
#app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap()


#from main import views
#from main import errors

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #from .requests import configure_request
    #configure_request(app)


    return app