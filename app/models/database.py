# DATABASE.PY

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


deluser = "DROP TABLE users IF EXISTS"
delproducts = "DROP TABLE products IF EXISTS"
delsales = "DROP TABLE sales IF EXISTS"


queries = [query1, query2, query3]

deletes = [deluser, delproducts, delsales]