'''Handles all the product queries from the database'''

import json
from database import ProductsTable
from __init__ import dbconnect, createTables



class Products:
    def __init__(self):
        self.id = id
        self.price = price
        self.quantity = quantity
        self.category = category
        self.productname = productname
        self.description = description

    def save(self):
        '''takes the data input from the user and saves it into the database'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "INSERT INTO products (id,productname,description, category, quantity, price) VALUES(%s, %s, %s, %s, %s,%s);"
        data = (self.id, self.productname, self.description, self.category, self.quantity, self.price)
        cur.execute(query, data)
        conn.commit()
        cur.close()

    def viewall(self):
        '''queries the database to view all products'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("SELECT * FROM products;")
        cur.close()

    def viewone(self):
        '''queries the database to view one product'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "SELECT * FROM products WHERE id=(%s)"
        data = (self.id,)
        cur.execute(query,data)
        cur.close()

    def ammend(self):
        '''method that updates product data in the database'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "UPDATE products SET (%s) WHERE id=(%s);"
        data = (quantity += self.quantity, self.id)
        cur.execute(query, data)
        conn.commit()
        cur.close()


    def delete(self):
        conn= dbconnect()
        cur= conn.cursor()
        '''method that deletes a record from the database'''
        query = "DELETE FROM products WHERE id=(%s) CASCADE;"
        data = (self.id,)
        cur.execute(query, data)
        conn.commit()
        cur.close()
