#DATABASE.PY


import psycopg2
import psycopg2.extras as extra



query1 = """CREATE TABLE IF NOT EXISTS users(id serial PRIMARY KEY,
                                            username text NOT NULL ,
                                            email text NOT NULL,
                                            password text NOT NULL,
                                            admin_role bool NOT NULL);"""


query2 = """CREATE TABLE IF NOT EXISTS products(id serial PRIMARY KEY,
                    productname text NOT NULL ,
                    description text NOT NULL ,
                    category text NOT NULL ,
                    quantity INTEGER NOT NULL,
                    price INTEGER NOT NULL);"""


query3 = """CREATE TABLE IF NOT EXISTS sales(id serial PRIMARY KEY,
                    productname text NOT NULL ,
                    quantity INTEGER NOT NULL,
                    price INTEGER NOT NULL,
                    date_sold TIMESTAMP);"""


queries = [query1, query2, query3]
