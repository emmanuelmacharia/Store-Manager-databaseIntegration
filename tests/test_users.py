import unittest
from app import create_app
import json
from .baseTest import BaseTestClient
from app.views.user import Users, Signin, Logout


class TestProducts(BaseTestClient):
    def test_empty_username_registration_login(self):
        """tests whether the username provided is an empty string"""
        response = self.app.post(
            self.registration_url,
            data=json.dumps(self.test_empty_username),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        self.assertEqual(data["message"], "please use the right format")
        self.assertEqual(response.status_code, 400)

    def test_empty_email_registration_login(self):
        """tests whether the username provided is an empty string"""
        response = self.app.post(
            self.registration_url,
            data=json.dumps(self.test_empty_email),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        self.assertEqual(data["message"], "please use the right format")
        self.assertEqual(response.status_code, 400)

    def test_empty_password_registration_login(self):
        """tests whether the username provided is an empty string,
        returns an error message"""
        response = self.app.post(
            self.registration_url,
            data=json.dumps(self.test_empty_password),
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
            data=json.dumps(self.test_invalid_password),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        self.assertEqual(data["message"], "please use the right format")
        self.assertEqual(response.status_code, 400)

    def test_register_success(self):
        """tests whether the username,
        password and email provided are valid, returns 201"""
        response = self.app.post(
            self.registration_url,
            data=json.dumps(self.test_valid_input),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        self.assertEqual(data["message"], "new user created")
        self.assertEqual(response.status_code, 201)

    def test_login_success(self):
        """tests whether the input provided matches with an existing user,
        and returns 200 upon login success"""
        test_user = self.register()
        test_user = self.test_valid_input
        response = self.app.post(
            "api/v2/login", data=json.dumps(test_user),
            content_type="application/json"
        )
        data = json.loads(response.data.decode())
        self.assertEqual(data["message"], "signin successful")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main(exit=False)
