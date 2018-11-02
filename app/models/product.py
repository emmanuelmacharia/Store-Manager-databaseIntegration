"""Handles all the product queries from the database"""

import json
from ..models import dbconnect

conn = dbconnect()
cur = conn.cursor()


class Product:
    def __init__(self, productname, description, category, quantity, price):
        self.productname = productname
        self.description = description
        self.category = category
        self.quantity = quantity
        self.price = price

    def save(self):
        """takes the data input from the user and saves it into the database"""
        conn = dbconnect()
        cur = conn.cursor()
        query = """INSERT INTO products
                (productname,description, category, quantity, price)
                VALUES('%s', '%s', '%s' , '%s', '%s');""" % (
            self.productname,
            self.description,
            self.category,
            self.quantity,
            self.price,
        )
        cur.execute(query)
        result = cur.execute(
            "SELECT * FROM products\
            WHERE productname = '%s';" % (self.productname)
        )
        conn.commit()
        cur.close()
        return {"message": "product successfully created",
                "products": result}, 201

    def viewall(self):
        """queries the database to view all products"""
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products;")
        return_records = cur.fetchall()
        cur.close()
        records = []
        for record in return_records:
            record_format = {
                'id': record[0],
                'productname': record[1],
                'description': record[2],
                'category': record[3],
                'quantity': record[4],
                'price': record[-1]
            }
        records.append(record_format)
        return {
            'message': 'products successfully retrieved',
            'products': records
            }

    @staticmethod
    def viewone(id):
        """queries the database to view one product"""
        conn = dbconnect()
        cur = conn.cursor()
        query = "SELECT * FROM products WHERE id= %s"
        cur.execute(query, (id, ))
        record = cur.fetchone()
        cur.close()
        if record is None:
            return (
                {"message": "No product by that id found, review input"},
                404
            )
        else:
            record_format = {
                "id": record[0],
                "productname": record[1],
                "desctription": record[2],
                "category": record[3],
                "quantity": record[4],
                "price": record[5]
            }
            return {'message': 'product requested', 'products': record_format}, 200


    @staticmethod
    def ammend(productname, description, category, quantity, price):
        """method that updates product data in the database"""
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("""UPDATE products
                    SET productname = %s, description = %s,
                    category = %s,  quantity = %s, price = %s
                    WHERE productname=%s""", (
           productname, description, category, quantity, price, productname
        ))
        conn.commit()

    def get_by_price(self, productname):
        '''Get single product by its price'''
        conn = dbconnect()
        cur.execute("SELECT * FROM products\
                    WHERE productname = %s", (productname, ))
        product = cur.fetchone()
        return product[-1]

    def get_quantity(self, productname):
        '''get single produt's quantity'''
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM products
        WHERE productname= %s""", (productname, ))
        stock = cur.fetchone()
        return stock[-2]


    @staticmethod
    def delete(id):
        """method that deletes a record from the database"""
        conn = dbconnect()
        cur = conn.cursor()
        viewone(id)
        if viewone.record is None:
            return {'message': 'Product doesn\'t exist'}, 404
        query = "DELETE FROM products WHERE id = %s;" % (id,)
        cur.execute(query)
        conn.commit()
        cur.close()
        return {"message": "product deleted successfully"}, 200
