import sqlite3

class TransactionManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def create_transaction(self, product_id, user_id, quantity):
        query = '''INSERT INTO Transactions (ProductID, UserID, Quantity, TransactionDate, Status) VALUES (?, ?, ?, CURRENT_TIMESTAMP, 'Completed')'''
        self.conn.execute(query, (product_id, user_id, quantity))
        self.conn.commit()

    def read_transaction(self, transaction_id):
        query = '''SELECT * FROM Transactions WHERE TransactionID = ?'''
        cursor = self.conn.execute(query, (transaction_id,))
        return cursor.fetchone()
    
    def get_all_transactions(self):
        query = '''SELECT * FROM Transactions'''
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def update_transaction(self, transaction_id, product_id, user_id, quantity):
        query = '''UPDATE Transactions SET ProductID = ?, UserID = ?, Quantity = ? WHERE TransactionID = ?'''
        self.conn.execute(query, (product_id, user_id, quantity, transaction_id))
        self.conn.commit()

    def delete_transaction(self, transaction_id):
        query = '''UPDATE Transactions SET Status = 'Cancelled', Date_Cancelled = CURRENT_TIMESTAMP WHERE TransactionID = ?'''
        self.conn.execute(query, (transaction_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()