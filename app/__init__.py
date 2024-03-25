from flask import Flask # Import the Flask class from the flask module


# Create an instance of Flask called app which will be the central object
app = Flask(__name__)

# import the routes to the app
from . import routes