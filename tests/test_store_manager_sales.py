from .baseTest import BaseTest
from .data import *


class TestSale(BaseTest):
    def test_get_admin_sales(self):
        """Tests the get (view all) sales method for the admin, asserts true
        if the test passes and gives a status code of 200"""
        test_user = BaseTest.register()
        test_user = BaseTest.signin()
        response = self.app.get(
            sales_url,
            headers=dict(Authorization="Bearer " + test_user),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_get_attendant_sales(self):
        """Tests the get sales method by the attendant for the attendant"""
        test_user = BaseTest.register()
        test_user = BaseTest.signin()
        response = self.app.get(
            sales_url,
            headers=dict(Authorization="Bearer " + test_user),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_single_sale_found(self):
        """Tests whether the sale with the id provided is there,
        returns status_code 404"""
        test_user = BaseTest.register()
        test_user = BaseTest.signin()
        response = self.app.post(
            sales_url,
            headers=dict(Authorization="Bearer " + test_user),
            data=json.dumps(test_valid_sale),
            content_type="application/json",
        )
        response = self.app.get(
            "api/v2/sales/1",
            headers=dict(Authorization="Bearer " + test_user),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_post_sales(self):
        """Tests whether the attendant can successfully create a new sale
        (POST method); asserts true if the test passes and status code=201"""
        test_user = BaseTest.register()
        test_user = BaseTest.signin()
        response = self.app.post(
            sales_url,
            headers=dict(Authorization="Bearer " + test_user),
            data=json.dumps(test_valid_sale),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_no_sale_found(self):
        """Tests for non existent items"""
        test_user = BaseTest.register()
        test_user = BaseTest.signin()
        response = self.app.get(
            not_found_single_sale_url,
            headers=dict(Authorization="Bearer " + test_user),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 404)