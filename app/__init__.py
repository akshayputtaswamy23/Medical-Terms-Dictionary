# app/__init__.py

from flask import Flask

# Create the app instance
app = Flask(__name__)

# Import the routes after app creation to avoid circular imports
from app import routes
