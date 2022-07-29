from flask import Flask
from .views import products


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.register_blueprint(products.bp)
    return app
