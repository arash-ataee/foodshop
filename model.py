import psycopg2

conn = psycopg2.connect(database='foodshop', user='arash', password='123212', host='127.0.0.1', port='5432')

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS customer
(ID SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
address TEXT NOT NULL
);""")


cur.execute("""CREATE TABLE IF NOT EXISTS food
(ID SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL UNIQUE,
category VARCHAR(255) NOT NULL,
price integer NOT NULL
);""")


cur.execute("""CREATE TABLE IF NOT EXISTS shop
(ID SERIAL PRIMARY KEY,
food integer REFERENCES food(ID) ON DELETE RESTRICT,
customer integer REFERENCES customer(ID) ON DELETE RESTRICT,
number integer NOT NULL
);""")


cur.execute("""CREATE TABLE IF NOT EXISTS message
(customer integer REFERENCES customer(ID) NOT NULL,
food integer REFERENCES food(ID) NOT NULL,
rate VARCHAR(1) NOT NULL,
text TEXT);""")


conn.commit()
conn.close()


class Customer:

    def __init__(self, name, address):
        co = psycopg2.connect(database='foodshop', user='arash', password='123212', host='127.0.0.1', port='5432')
        cu = co.cursor()
        cu.execute("INSERT INTO customer (name, address) \
        VALUES ('{0}', '{1}')".format(name, address))
        co.commit()
        co.close()


class Food:

    def __init__(self, name, category, price):
        co = psycopg2.connect(database='foodshop', user='arash', password='123212', host='127.0.0.1', port='5432')
        cu = co.cursor()
        cu.execute("INSERT INTO food (name, category, price) \
        VALUES ('{0}', '{1}', {2})".format(name, category, price))
        co.commit()
        co.close()


class Shop:

    def __init__(self, food_id, customer_id, number):
        co = psycopg2.connect(database='foodshop', user='arash', password='123212', host='127.0.0.1', port='5432')
        cu = co.cursor()
        cu.execute("INSERT INTO shop (food, customer, number) \
        VALUES ({0}, {1}, {2})".format(food_id, customer_id, number))
        co.commit()
        co.close()


class Message:

    def __init__(self, customer_id, food_id, rate, text=None):
        co = psycopg2.connect(database='foodshop', user='arash', password='123212', host='127.0.0.1', port='5432')
        cu = co.cursor()
        cu.execute("INSERT INTO message (customer, food, rate, text) \
        VALUES ({0}, {1}, {2}, '{3}')".format(customer_id, food_id, rate, text))
        co.commit()
        co.close()
