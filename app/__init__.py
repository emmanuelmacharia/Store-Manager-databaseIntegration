from flask import Blueprint, Flask
from instance.config import *
from flask_restful import Api, Resource
from app.api.v1.views import AdminProducts, AttendantProducts, AttendantSales, AdminSale, Sale, Product, Register, Login
from flask_jwt_extended import JWTManager
from app.api.v2.models import dbconnect, createTables
from app.api.v2.views.product import Products
from app.api.v2.views.user import Users
from app.api.v2.views.sale import Sales



v1 = Blueprint('v1',__name__,url_prefix='/api/v1')
api = Api(v1)
v2 = Blueprint('v2',__name__, url_prefix='/api/v2')
database = Api(v2)


def create_app(config_name):

    app = Flask(__name__, instance_relative_config = True)
    app.config.from_object(app_configurations['development'])

    app.config['SECRET_KEY'] = 'a-little-crazy-story'
    dbconnect()
    createTables()

    jwt = JWTManager(app)

    api.add_resource(AdminProducts, '/admin/products')
    api.add_resource(AttendantProducts, '/attendant/products')
    api.add_resource(AttendantSales, '/attendant/sales')
    api.add_resource(AdminSale, '/admin/sales')
    api.add_resource(Sale, '/admin/sales/<int:id>')
    api.add_resource(Product, '/products/<int:id>')
    api.add_resource(Register, '/register')
    api.add_resource(Login, '/login')

    #ENDPOINTS FOR V2
    database.add_resource(Users, '/auth/signup')
    database.add_resource(Products, '/products')
    database.add_resource(Sales, '/sales')

    app.register_blueprint(v1)
    app.register_blueprint(v2)
    return app
