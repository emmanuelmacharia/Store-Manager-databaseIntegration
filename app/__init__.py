"""Initializes and creates the app as one function"""

import os

from flask import Blueprint, Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource

from .models import dbconnect, createTables
from instance.config import app_configurations
from .views.product import Products, SingleProduct
from .views.user import Users, Signin
from .views.sale import Sales


# v1 = Blueprint("v1", __name__, url_prefix="/api/v1")
# api = Api(v1)
v2 = Blueprint("v2", __name__, url_prefix="/api/v2")
api = Api(v2)


def create_app(config_name):
    """Runs the entire appliation"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_configurations["development"])
    os.getenv("DATABASE_URL")
    os.getenv("SECRET_KEY")
    dbconnect()
    createTables()



    # ENDPOINTS FOR V2
    api.add_resource(Users, "/auth/signup")
    api.add_resource(Products, "/products")
    api.add_resource(Sales, "/sales")
    api.add_resource(Signin, "/auth/login")
    api.add_resource(SingleProduct, "/product/<int:id>")


    app.register_blueprint(v2)
    return app
