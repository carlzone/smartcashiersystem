import sqlite3
import hashlib

class UserManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def create_user(self, username, password, role):
        # Encrypt the password using MD5
        encrypted_password = hashlib.md5(password.encode()).hexdigest()
        query = '''INSERT INTO Users (Username, Password, Role, Status, Date_Created) VALUES (?, ?, ?, 'Active', CURRENT_TIMESTAMP)'''
        self.conn.execute(query, (username, encrypted_password, role))
        self.conn.commit()

    def read_user(self, user_id):
        query = '''SELECT * FROM Users WHERE UserID = ?'''
        cursor = self.conn.execute(query, (user_id,))
        return cursor.fetchone()
    
    def read_all_users(self):
        query = '''SELECT * FROM Users'''
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def update_user(self, user_id, username, password, role):
        query = '''UPDATE Users SET Username = ?, Password = ?, Role = ? WHERE UserID = ?'''
        self.conn.execute(query, (username, password, role, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        query = '''UPDATE Users SET Status = 'Removed', Date_Removed = CURRENT_TIMESTAMP WHERE UserID = ?'''
        self.conn.execute(query, (user_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()