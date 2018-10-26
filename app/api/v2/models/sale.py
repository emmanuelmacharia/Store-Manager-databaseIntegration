'''Handles all the product queries from the database'''

import json
from .__init__ import dbconnect, createTables



class Sale:
    def __init__(self):
        self.price = price
        self.quantity = quantity
        self.category = category
        self.productname = productname
        self.description = description

    def save(self):
        '''takes the data input from the user and saves it into the database'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("INSERT INTO sales (id,productname,description, category, quantity, price) VALUES('%s, %s, %s, %s, %s,%s');")
        cur.close()

    def viewall(self):
        '''queries the database to view all sales'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("SELECT * FROM sales;")
        cur.close()

    def viewone(self):
        '''queries the database to view one product'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "SELECT * FROM sales WHERE id=self.id"
        data = (self.id,)
        cur.execute(query, data)
        cur.close()

    def ammend(self):
        '''method that updates product data in the database'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "UPDATE sales SET '%s' WHERE id=(%s);"
        data = (self.price, self.id)
        cur.execute(query, data)
        conn.commit()
        cur.close()

    def delete(self):
        '''method that deletes a record from the database'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "DELETE FROM sales WHERE id=(%s) CASCADE;"
        data = (self.id,)
        cur.execute(query, data)
        cur.commit()
