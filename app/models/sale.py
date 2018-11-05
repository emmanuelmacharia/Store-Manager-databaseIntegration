"""Handles all the sales queries from the database"""

import json
from ..models import dbconnect


class Sale:
    """Contains the sales models"""
    def __init__(self, attendant, productname, quantity, price, date_sold):
        self.attendant = attendant
        self.productname = productname
        self.quantity = quantity
        self.price = price
        self.date_sold = date_sold

    def save(self):
        """takes the data input from the user and saves it into the database"""
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO sales (attendant, productname, quantity, price, date_sold)
            VALUES(%s,%s, %s, %s, %s);""",
            (self.attendant, self.productname,
                self.quantity, self.price, str(self.date_sold))
        )
        conn.commit()
        cur.close()

    def serializer(self):
        return dict(
            attendant=self.attendant,
            productname=self.productname,
            quantity=self.quantity,
            price=self.price
        )

    def viewall(self):
        """queries the database to view all sales"""
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM sales;")
        sales = cur.fetchall()
        all_sales = []
        for sale in sales:
            all_sales.append(sale)
        cur.close()
        return all_sales

    def viewone(self):
        """queries the database to view one product"""
        conn = dbconnect()
        cur = conn.cursor()
        query = "SELECT * FROM sales WHERE id=self.id"
        data = (self.id,)
        cur.execute(query, data)
        cur.close()

    def delete(self, id):
        """method that deletes a sale record from the database"""
        conn = dbconnect()
        cur = conn.cursor()
        query = "DELETE FROM sales WHERE id=(%s) CASCADE;" % (id,)
        cur.execute(query)
        conn.commit()
        cur.close()
