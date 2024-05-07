import os
from flask import Flask
from .views import configure_routes

def create_app():
    app = Flask(__name__)
     # Generate a random secret key
    SECRET_KEY = os.urandom(24)
    print("🚀 ~ SECRET_KEY:", SECRET_KEY.hex())
    app.config['SECRET_KEY'] = SECRET_KEY.hex()

    configure_routes(app)

    return app
