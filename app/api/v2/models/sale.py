'''Handles all the product queries from the database'''

import json
from __init__ import dbconnect, createTables



class Sale:
    def __init__(self):
        self.price = price
        self.quantity = quantity
        self.category = category
        self.productname = productname
        self.description = description

    def save(self):
        '''takes the data input from the user and saves it into the database'''
        cur.execute("INSERT INTO sales (id,productname,description, category, quantity, price) VALUES('%d, %s, %s, %s, %d,%d');")


    def viewall(self):
        '''queries the database to view all sales'''
        cur.execute("SELECT * FROM sales;")
        cur.commit()

    def viewone(self):
        '''queries the database to view one product'''
        cur.execute("SELECT * FROM sales WHERE id=self.id")

    def ammend(self):
        '''method that updates product data in the database'''
        cur.execute("UPDATE sales SET '%S' WHERE id=self.id;")
        cur.commit()


    def delete(self):
        '''method that deletes a record from the database'''
        cur.execute("DELETE FROM sales WHERE id=self.id CASCADE;")
        cur.commit()
