'''Handles all the product queries from the database'''

import json
from .__init__ import dbconnect, createTables



class Product:
    def __init__(self, productname,description,category,quantity,price):
        self.productname = productname
        self.description = description
        self.category = category
        self.quantity = quantity
        self.price = price

    def save(self):
        '''takes the data input from the user and saves it into the database'''
        conn= dbconnect()
        cur= conn.cursor()
        # selected = cur.execute("SELECT * FROM products WHERE id=(%s)"(id))
        query = """INSERT INTO products
                (productname,description, category, quantity, price)
                VALUES('%s', %s, %s, %s, %s);""" %(self.productname, self.description,self.category, self.quantity, self.price)
        cur.execute(query)
        conn.commit()
        cur.close()

    def viewall():
        '''queries the database to view all products'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("SELECT * FROM products;")
        cur.fetchall()
        cur.close()

    def viewone():
        '''queries the database to view one product'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "SELECT * FROM products WHERE id=(%s)"
        data = (id,)
        cur.execute(query,data)
        cur.fetchone()
        cur.close()

    def ammend( productname,description, category, price):
        '''method that updates product data in the database'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "UPDATE products SET (productname,description, category, price) WHERE id=(%s);"
        data = ( productname,  description,  category,  price)
        cur.execute(query, data)
        conn.commit()
        cur.close()

    def modifyquantity(quantity):
        conn = dbconnect()
        cur = conn.cursor()
        query = "UPDATE products SET (quantity) WHERE id=(%s);"
        quantity +=  quantity
        data = (quantity,  id)
        cur.execute(query, data)
        conn.commit()
        cur.close()

    def delete(id):
        conn= dbconnect()
        cur= conn.cursor()
        '''method that deletes a record from the database'''
        query = "DELETE FROM products WHERE id=(%s) CASCADE;"
        data = (id,)
        cur.execute(query, data)
        conn.commit()
        cur.close()
