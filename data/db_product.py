# db_product.py

import sqlite3

class ProductManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def create_product(self, name, price, quantity, type):
        query = '''INSERT INTO Products (ProductName, Price, Quantity, QuantityType, Status) VALUES (?, ?, ?, ?, 'Available')'''
        self.conn.execute(query, (name, price, quantity, type))
        self.conn.commit()

    def read_product(self, product_id):
        query = '''SELECT * FROM Products WHERE ProductID = ?'''
        cursor = self.conn.execute(query, (product_id))
        return cursor.fetchone()
    
    def get_products_by_name(self, name):
        query = '''SELECT * FROM Products WHERE ProductName LIKE ?'''
        name_pattern = '%' + name + '%'
        cursor = self.conn.execute(query, (name_pattern,))
        return cursor.fetchall()

    def get_all_products(self):
        query = '''SELECT * FROM Products'''
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def get_products_by_page(self, page_number=1):
        offset = (page_number - 1) * 10
        query = '''SELECT * FROM Products LIMIT 10 OFFSET ?'''
        cursor = self.conn.execute(query, (offset,))
        return cursor.fetchall()

    def update_product(self, product_id, name, price, quantity):
        query = '''UPDATE Products SET ProductName = ?, Price = ?, Quantity = ? WHERE ProductID = ?'''
        self.conn.execute(query, (name, price, quantity, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        query = '''UPDATE Products SET Status = 'Removed', Date_Removed = CURRENT_TIMESTAMP WHERE ProductID = ?'''
        self.conn.execute(query, (product_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()