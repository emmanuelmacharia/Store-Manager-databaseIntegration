#DATABASE.PY


import psycopg2
import psycopg2.extras as extra



query1 = """CREATE TABLE IF NOT EXISTS users(id serial PRIMARY KEY NOT NULL,
                                            username text NOT NULL ,
                                            email text NOT NULL,
                                            password text NOT NULL,
                                            role text NOT NULL);"""


query2 = """CREATE TABLE IF NOT EXISTS products(id serial PRIMARY KEY NOT NULL,
                    productname text NOT NULL ,
                    description text NOT NULL ,
                    category text NOT NULL ,
                    quantity INTEGER NOT NULL,
                    price INTEGER NOT NULL);"""


query3 = """CREATE TABLE IF NOT EXISTS sales(id serial PRIMARY KEY NOT NULL,
                    productname text NOT NULL ,
                    description text NOT NULL ,
                    category text NOT NULL ,
                    quantity INTEGER NOT NULL,
                    price INTEGER NOT NULL);"""


queries = [query1, query2, query3]
