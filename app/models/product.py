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
        records = cur.fetchall()
        cur.close()
        all_products = []
        for record in records:
            all_products.append(record)
        return all_products

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
                404,
            )
        else:
            return (
                [record[0], record[1], record[2],
                    record[3], record[4], record[-1]],
                200
            )

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

    @staticmethod
    def delete(id):
        """method that deletes a record from the database"""
        conn = dbconnect()
        cur = conn.cursor()
        query = "DELETE FROM products WHERE id = %s;" % (id,)
        cur.execute(query)
        conn.commit()
        cur.close()
        return {"message": "product deleted successfully"}, 200
