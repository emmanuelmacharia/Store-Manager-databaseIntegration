
import unittest
from app import create_app
import json

class BaseTestClient(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing').test_client()

    self.user_information = {
        "username":"Spongebob",
        "email": "spongebobsquarepants@bikinibottom.sea",
        "password": "CrustyKr1abs"
    }

    self.test_valid_product = {
        "name" : "hp",
        "description" : "elite",
        "category" : "computers",
        "quantity" : 10,
        "price" : 50000
        }

    self.test_empty_username= {
        "username":"",
        "email":"user@inlook.com",
        "password": "fdkff5A"
        }
    self.test_empty_email = {
        "username":"user",
        "email":"",
        "password": "fdkff5A"
        }
    self.test_empty_password = {
        "username":"user",
        "email":"solomarsha@outlook.com",
        "password": ""
        }
    self.test_invalid_password = {
        "username":"user",
        "email":"solomarsha@outlook.com",
        "password": "pass"
        }
    self.test_valid_input= {
        "username":"user",
        "email":"solomarsha@outlook.com",
        "password": "pass1Word"
        }
    self.test_login_success = {
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
