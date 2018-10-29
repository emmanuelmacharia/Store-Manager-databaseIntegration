'''Handles all the product queries from the database'''

import json
from .__init__ import dbconnect, createTables



class Sale:
    '''Contains the sales models'''
    def save(productname, quantity, price):
        '''takes the data input from the user and saves it into the database'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("INSERT INTO sales (productname,quantity, price) VALUES('%s', '%s' ,'%s');"%(productname,quantity,price))
        cur.close()

    def viewall():
        '''queries the database to view all sales'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("SELECT * FROM sales;")
        sales = cur.fetchall()
        all_sales = []
        for sale in sales:
            all_sales.append(sales)
        cur.close()
        return all_sales

    def viewone():
        '''queries the database to view one product'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "SELECT * FROM sales WHERE id=self.id"
        data = (self.id,)
        cur.execute(query, data)
        cur.close()

    def ammend():
        '''method that updates product data in the database'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "UPDATE sales SET '%s' WHERE id=(%s);"
        data = (self.price, self.id)
        cur.execute(query, data)
        conn.commit()
        cur.close()

    def delete(id):
        '''method that deletes a record from the database'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "DELETE FROM sales WHERE id=(%s) CASCADE;"%(id,)
        cur.execute(query)
        conn.commit()
        cur.close()
