"""Initializes and creates the app as one function"""

import os

from flask import Blueprint, Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource

from .models import dbconnect, createTables
from instance.config import app_configurations
from .views.product import Products, SingleProduct
from .views.user import Users, Signin, Logout, blacklist
from .views.sale import Sales
from .models.user import User


v2 = Blueprint("v2", __name__, url_prefix="/api/v2")
api = Api(v2)


def create_app(config):
    """Runs the entire appliation"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_configurations['development'])
    os.getenv("SECRET_KEY")
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
    app.config['JWT_SECRET_KEY'] = os.getenv("SECRET_KEY")
    jwt = JWTManager(app)
    dbconnect()
    createTables()
    username = 'emmanuel macharia'
    email = 'emmanuel@sote.com'
    admin_role = True
    password = '123Qwerty'
    User.createadmin(username, email, password, admin_role)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in blacklist

    # ENDPOINTS FOR V2
    api.add_resource(Users, "/auth/signup")
    api.add_resource(Products, "/products")
    api.add_resource(Sales, "/sales")
    api.add_resource(Signin, "/auth/login")
    api.add_resource(SingleProduct, "/product/<int:id>")
    api.add_resource(Logout, "/auth/logout")

    app.register_blueprint(v2)
    return app
