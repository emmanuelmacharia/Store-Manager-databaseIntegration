# DATABASE.PY

query1 = """CREATE TABLE IF NOT EXISTS users(id serial PRIMARY KEY,
                                            username text NOT NULL,
                                            email text NOT NULL UNIQUE,
                                            password text NOT NULL,
                                            admin_role bool NOT NULL);"""


query2 = """CREATE TABLE IF NOT EXISTS products(id serial PRIMARY KEY,
                    productname text NOT NULL UNIQUE,
                    description text NOT NULL ,
                    category text NOT NULL ,
                    quantity INTEGER NOT NULL,
                    price INTEGER NOT NULL);"""


query3 = """CREATE TABLE IF NOT EXISTS sales(id serial PRIMARY KEY,
                    attendant text NOT NULL,
                    productname text NOT NULL ,
                    quantity INTEGER NOT NULL,
                    price INTEGER NOT NULL,
                    date_sold TIMESTAMP NOT NULL);"""


deluser = "DROP TABLE users"
delproducts = "DROP TABLE products"
delsales = "DROP TABLE sales"

nonduplicate = "CREATE EXTENSION IF NOT EXISTS citext;"

alter = "ALTER TABLE products ALTER COLUMN productname TYPE citext;"

queries = [query1, query2, query3, nonduplicate, alter]

deletes = [deluser, delproducts, delsales]
