import sqlite3

def creating_db():
    def connect_to_db():
        conn = sqlite3.connect('website.db')
        c = conn.cursor()
        return c, conn

    def creating_db_users(c, conn):

        # creating main table(currently place holder)
        c.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        mass INTEGER,
        age INTEGER,
        height INTEGER,
        gender TEXT,
        goal TEXT,
        account_created_date DATE,
        best_streak INTEGER,
        current_streak INTEGER,
        days_when_on_site INTEGER,
        added_produckts INTEGER,
        pr_chest INTEGER
       )
        ''')
        conn.commit()

    def creating_test_data(c, conn):
        c.execute('''
        INSERT INTO users (username, email, password, mass, age, height)
        VALUES ('qw','amogus@gmail.com', 'qw', 50, 20, 180)
        ''')
        c.execute('''
        INSERT INTO users (username,email, password)
        VALUES ('zx','amogus@gmail.pl', 'zx')
        ''')
        conn.commit()


    def creating_db_products(c, conn):
            # creating products table(currently place holder)
            # prdukty to powina byc wartosc na 100g
            # jednostki to kcal i g
        c.execute('''
            CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            company TEXT NOT NULL,
            shop TEXT NOT NULL,
            mass INTEGER NOT NULL,
            energy_value FLOAT NOT NULL,
            fat FLOAT NOT NULL,
            saturated_fat FLOAT NOT NULL,
            carbohydrates FLOAT NOT NULL,
            sugars FLOAT NOT NULL,
            fiber FLOAT NOT NULL,
            proteins FLOAT NOT NULL,
            salts FLOAT NOT NULL,
            rating FLOAT NOT NULL
            )
            ''')
        conn.commit()
    def products_table_test_data_init(c, conn):
        c.execute('''
            INSERT INTO products (name, company, shop, mass, energy_value, fat, saturated_fat, carbohydrates, sugars, fiber, proteins, salts, rating)
            VALUES ('Lód Tripple Joy BLUEBERRY','Marletto', 'Biedronka', 76, 377, 25, 17, 35, 31, 0.5, 3.1, 0.1, 9.0)
            ''')
        c.execute('''
            INSERT INTO products (name, company, shop, mass, energy_value, fat, saturated_fat, carbohydrates, sugars, fiber, proteins, salts, rating)
            VALUES ('Lód w rożku o smaku JAGODA','Marletto', 'Biedronka', 94, 292, 12, 8.9, 43, 34, 0.5, 3.5, 0.14, 9.8)
            ''')
        conn.commit()

    def db_test_query(c, conn):
        c.execute('SELECT * FROM products')
        rows = c.fetchall()
        for row in rows:
            print(row)

    if __name__ == '__main__':
        c,conn = connect_to_db()
        #creating_db_users(c,conn)
        #creating_test_data(c,conn)
        creating_db_products(c, conn)
        products_table_test_data_init(c, conn)
        db_test_query(c,conn)
        conn.close()

if __name__ == '__main__':
    creating_db()