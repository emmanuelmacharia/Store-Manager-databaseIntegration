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
        cur.execute("INSERT INTO products (id,productname,description, category, quantity, price) VALUES('%d, %s, %s, %s, %d,%d');")
        conn.commit()
        cur.close()

    def viewall(self):
        '''queries the database to view all products'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("SELECT * FROM products;")
        conn.commit()
        cur.close()

    def viewone(self):
        '''queries the database to view one product'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("SELECT * FROM products WHERE id=self.id")
        conn.commit()
        cur.close()

    def ammend(self):
        conn= dbconnect()
        cur= conn.cursor()
        '''method that updates product data in the database'''
        cur.execute("UPDATE products SET '%S' WHERE id=self.id;")
        conn.commit()
        cur.close()


    def delete(self):
        conn= dbconnect()
        cur= conn.cursor()
        '''method that deletes a record from the database'''
        cur.execute("DELETE FROM products WHERE id=self.id CASCADE;")
        conn.commit()
        cur.close()
