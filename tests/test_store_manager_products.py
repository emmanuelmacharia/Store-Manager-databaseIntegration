from .baseTest import BaseTest
from .data import *


class TestProducts(BaseTest):
    def test_get_all_products(self):
        """tests get products endpoint"""
        test_user = Basetest.register()
        test_user = Basetest.signin()
        response = self.app.get(
            products_url,
            headers=dict(Authorization="Bearer " + test_user),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_post_products(self):
            test_user = Basetest.register()
            test_user = Basetest.signin()
            response = self.app.post(
                products_url,
                headers=dict(Authorization="Bearer " + test_user),
                data=json.dumps(test_valid_product),
                content_type="application/json",
            )
            self.assertEqual(response.status_code, 201)

    def test_single(self):
        test_user = Basetest.register()
        test_user = Basetest.signin()
        response = self.app.get(
            single_product_url,
            headers=dict(Authorization="Bearer " + test_user),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_no_products_found(self):
        test_user = Basetest.register()
        test_user = Basetest.signin()
        response = self.app.post(
            products_url,
            headers=dict(Authorization="Bearer " + test_user),
            data=json.dumps(test_valid_product),
            content_type="application/json",
        )
        response = self.app.get(
            not_found_single_product_url,
            headers=dict(Authorization="Bearer " + test_user),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)

    def test_cant_delete_product(self):
        pass

    