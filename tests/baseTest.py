
import unittest
from app import create_app
import json
from app.models import dbconnect, droptables

class BaseTestClient(unittest.TestCase):
    '''the base test configurations for the entire application'''
    def __init__(self):
        pass

    def setUp(self):
        '''creates the data required in the tests. also connects to the test database where the data will be stored'''
        dbconnect()
        self.app = create_app('testing').test_client()

    user_information = {
        "username":"Spongebob",
        "email": "spongebobsquarepants@bikinibottom.sea",
        "password": "CrustyKr1abs"
    }

    test_valid_product = {
        "name" : "hp",
        "description" : "elite",
        "category" : "computers",
        "quantity" : 10,
        "price" : 50000
        }

    test_empty_username= {
        "username":"",
        "email":"user@inlook.com",
        "password": "fdkff5A"
        }
    test_empty_email = {
        "username":"user",
        "email":"",
        "password": "fdkff5A"
        }
    test_empty_password = {
        "username":"user",
        "email":"solomarsha@outlook.com",
        "password": ""
        }
    test_invalid_password = {
        "username":"user",
        "email":"solomarsha@outlook.com",
        "password": "pass"
        }
    test_valid_input= {
        "username":"user",
        "email":"solomarsha@outlook.com",
        "password": "pass1Word"
        }
    test_login_success = {
        "username":"user",
        "email":"solomarsha@outlook.com",
        "password": "pass1Word"
        }

    

    def register(self):
        '''registers the test client user'''
        test_register = self.app.post('api/v1/register', data= json.dumps(
                                        dict(user_information)),
                                        content_type = 'application/json')

        return json.loads(test_register.data.decode())["access_token"]

    def signin(self):
        '''signs the test client in so that we can run our tests'''
        test_signin = self.app.post('api/v1/login', data = json.dumps(
                                    dict(user_information)),
                                    content_type='application/json')
        return json.loads(test_signin.data.decode())["access_token"]
