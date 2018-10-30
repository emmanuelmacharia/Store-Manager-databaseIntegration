"""Handles all the product queries from the database"""

import json
from ..models import dbconnect


class Product:
    # def __init__( productname,description,category,quantity,price):
    # self.productname = productname
    # self.description = description
    # self.category = category
    # self.quantity = quantity
    # self.price = price
    # pass

    def save(self, productname, description, category, quantity, price):
        """takes the data input from the user and saves it into the database"""
        conn = dbconnect()
        cur = conn.cursor()
        # selected = cur.execute("SELECT * FROM products WHERE id=(%s)"(id))
        query = """INSERT INTO products
                (productname,description, category, quantity, price)
                VALUES('%s', '%s', '%s' , '%s', '%s');""" % (
            productname,
            description,
            category,
            quantity,
            price,
        )
        cur.execute(query)
        result = cur.execute(
            "SELECT * FROM products WHERE productname = '%s';" % (productname)
        )
        conn.commit()
        cur.close()
        return {"message": "product successfully created", "products": result}, 201

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
        # (
        #     (record[0], record[1], record[2], record[3], record[4], record[-1]),
        #     200,
        # )

    def viewone(self, id):
        """queries the database to view one product"""
        conn = dbconnect()
        cur = conn.cursor()
        query = "SELECT * FROM products WHERE id='%s'" % (id,)
        cur.execute(query)
        record = cur.fetchone()
        cur.close()
        single_product = []
        if record == None:
            return (
                {"message": "No product by that id found, kindly review your input"},
                404,
            )
        else:
            return (
                [record[0], record[1], record[2], record[3], record[4], record[-1]],
                200,
            )

    def ammend(productname, description, category, price):
        """method that updates product data in the database"""
        conn = dbconnect()
        cur = conn.cursor()
        query = """UPDATE products
                    SET (productname= '%s',description = '%s', category = '%s', price = '%s')
                    WHERE productname='%s';""" % (
            productname,
            description,
            category,
            price,
            productname,
        )
        cur.execute(query)
        conn.commit()
        return_query = "SELECT * FROM products WHERE productname='%s'" % (productname,)
        cur.execute(return_query)
        record = cur.fetchone()
        cur.close()
        return (
            {
                "message": "product updated successfully",
                "product": ({
                    'id':record[0],
                    'productname':record[1],
                    'description':record[2],
                    'category':record[3],
                    'quantity':record[4],
                    'price':record[-1]}
                ),
            },
            202,
        )

    def modifyquantity(quantity, productname):
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE productname= '%s';" % (productname))
        result = cur.fetchone()
        quantity += int(result[4])
        query = "UPDATE products SET quantity= '%s' WHERE productname='%s';" % (
            quantity,
            productname,
        )
        cur.execute(query)
        conn.commit()
        return_query = "SELECT * FROM products WHERE productname='%s';" % (productname,)
        cur.execute(return_query)
        record = cur.fetchone()
        cur.close()
        return (
            {
                "message": "product updated successfully",
                "product": [
                    record[0],
                    record[1],
                    record[2],
                    record[3],
                    record[4],
                    record[-1],
                ],
            },
            202,
        )

    def delete(id):
        conn = dbconnect()
        cur = conn.cursor()
        """method that deletes a record from the database"""
        query = "DELETE FROM products WHERE id = %s;" % (id,)
        cur.execute(query)
        conn.commit()
        cur.close()
        return {"message": "product deleted successfully"}, 204
