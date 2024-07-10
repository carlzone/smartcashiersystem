import sqlite3

class SalesManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def create_sale(self, product_id, quantity):
        query = '''INSERT INTO Sales (ProductID, Quantity, SaleDate, Status) VALUES (?, ?, CURRENT_TIMESTAMP, 'Completed')'''
        self.conn.execute(query, (product_id, quantity))
        self.conn.commit()

    def read_sale(self, sale_id):
        query = '''SELECT * FROM Sales WHERE SaleID = ?'''
        cursor = self.conn.execute(query, (sale_id,))
        return cursor.fetchone()
    
    def get_all_sale(self, sale_id):
        query = '''SELECT * FROM Sales'''
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def update_sale(self, sale_id, product_id, quantity):
        query = '''UPDATE Sales SET ProductID = ?, Quantity = ? WHERE SaleID = ?'''
        self.conn.execute(query, (product_id, quantity, sale_id))
        self.conn.commit()

    def delete_sale(self, sale_id):
        query = '''UPDATE Sales SET Status = 'Cancelled', Date_Cancelled = CURRENT_TIMESTAMP WHERE SaleID = ?'''
        self.conn.execute(query, (sale_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()