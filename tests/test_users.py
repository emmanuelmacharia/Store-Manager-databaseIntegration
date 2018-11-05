import unittest
import json
from app import create_app
from app.views.product import Products, SingleProduct
from app.models.product import Product
from .data import *
from .baseTest import BaseTest


class TestUserEndpoints(BaseTest):
    '''Tests all user enpoints'''
    def test_user_registration(self):
        '''tests the registration endpoints'''
        response = self.data.post(
            '/api/v2/auth/signup', data=json.dumps(
                user_information
            ), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_empty_username_registration_login(self):
        """tests whether the username provided is an empty string"""
        response = self.app.post(
            registration_url,
            data=json.dumps(test_empty_username),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        self.assertEqual(data["message"], "please use the right format")
        self.assertEqual(response.status_code, 400)

    def test_empty_email_registration_login(self):
        """tests whether the username provided is an empty string"""
        response = self.app.post(
            registration_url,
            data=json.dumps(test_empty_email),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        self.assertEqual(data["message"], "please use the right format")
        self.assertEqual(response.status_code, 400)

    def test_empty_password_registration_login(self):
        """tests whether the username provided is an empty string,
        returns an error message"""
        response = self.app.post(
            registration_url,
            data=json.dumps(test_empty_password),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        self.assertEqual(data["message"], "please use the right format")
        self.assertEqual(response.status_code, 400)

    def test_invalid_password_registration_login(self):
        """tests whether the username provided is an empty string,
        returns an error message"""
        response = self.app.post(
            self.registration_url,
            data=json.dumps(test_invalid_password),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        self.assertEqual(data["message"], "please use the right format")
        self.assertEqual(response.status_code, 400)
