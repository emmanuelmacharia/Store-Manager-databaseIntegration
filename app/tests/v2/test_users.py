
import unittest
from app import create_app
import json
from baseTest import BaseTestClient

class TestProducts(BaseTestClient):
    '''''''
    def test_empty_username_registration_login(self):
        '''tests whether the username provided is an empty string, returns an error message'''
        #new_user = {"username":"", "email":"user@inlook.com","password": "fdkff5A"}
        response = self.app.post('api/v2/register',
                                    data = json.dumps(self.test_empty_username),
                                    content_type = 'application/json'
                                    )
        self.assertEqual(response.status_code, 400)

    def test_empty_email_registration_login(self):
        '''tests whether the username provided is an empty string, returns an error message'''
        #new_user = {"username":"user", "email":"", "password": "fdkff5A"}
        response = self.app.post('api/v2/register',
                                    data = json.dumps(self.test_empty_email),
                                    content_type = 'application/json'
                                    )
        self.assertEqual(response.status_code, 400)

    def test_empty_password_registration_login(self):
        '''tests whether the username provided is an empty string, returns an error message'''
        #new_user = {"username":"user", "email":"solomarsha@outlook.com","password": ""}
        response = self.app.post('api/v2/register',
                                    data = json.dumps(self.test_empty_password),
                                    content_type = 'application/json'
                                    )
        self.assertEqual(response.status_code, 400)

    def test_invalid_password_registration_login(self):
        '''tests whether the username provided is an empty string, returns an error message'''
        #new_user = {"username":"user", "email":"solomarsha@outlook.com","password": "pass"}
        response = self.app.post('api/v2/register',
                                    data = json.dumps(self.test_invalid_password),
                                    content_type = 'application/json'
                                    )
        self.assertEqual(response.status_code, 400)

    def test_register_success(self):
        '''tests whether the username, password and email provided are valid, returns 201'''
        response = self.app.post('api/v2/register',
                                    data = json.dumps(self.test_valid_input),
                                    content_type = 'application/json'
                                    )
        self.assertEqual(response.status_code, 201)

    def test_login_success(self):
        '''tests whether the input provided matches with an existing user, and returns 200 upon login success'''
        test_user = self.register()
        test_user = self.test_valid_input
        response = self.app.post('api/v2/login',
                                    data = json.dumps(test_user),
                                    content_type = 'application/json'
                                    )
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
unittest.main(exit= False)
