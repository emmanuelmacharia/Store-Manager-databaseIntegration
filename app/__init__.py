from flask import Blueprint, Flask
from instance.config import *
from flask_restful import Api, Resource
from app.api.v1.views import AdminProducts, AttendantProducts, AttendantSales, AdminSale, Sale, Product, Register, Login
from flask_jwt_extended import JWTManager


v1 = Blueprint('v1',__name__,url_prefix='/api/v1')
api = Api(v1)


def create_app(config_name):

    app = Flask(__name__, instance_relative_config = True)
    app.config.from_object(app_configurations['development'])
    app.register_blueprint(v1)
    app.config['SECRET_KEY'] = 'a-little-crazy-story'

    jwt = JWTManager(app)

    api.add_resource(AdminProducts, '/admin/products')
    api.add_resource(AttendantProducts, '/attendant/products')
    api.add_resource(AttendantSales, '/attendant/sales')
    api.add_resource(AdminSale, '/admin/sales')
    api.add_resource(Sale, '/admin/sales/<int:id>')
    api.add_resource(Product, '/products/<int:id>')

    api.add_resource(Register, '/register')
    api.add_resource(Login, '/login')
    return app
