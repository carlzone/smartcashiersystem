from data.db_product import ProductManager
from data.db_sale import SalesManager
from data.db_transaction import TransactionManager
from data.db_user import UserManager
import sqlite3

class DatabaseHelper:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
        self.product_manager = ProductManager(db_path)
        self.sales_manager = SalesManager(db_path)
        self.transaction_manager = TransactionManager(db_path)
        self.user_manager = UserManager(db_path)

        
    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS Users (
                                    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Username TEXT NOT NULL UNIQUE,
                                    Password TEXT NOT NULL,
                                    Role TEXT NOT NULL,
                                    Status TEXT NOT NULL,
                                    Date_Created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                    Date_Removed DATETIME);''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS Products (
                                    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    ProductName TEXT NOT NULL,
                                    Price REAL NOT NULL,
                                    Quantity INTEGER NOT NULL,
                                    QuantityType TEXT NOT NULL,
                                    Status TEXT NOT NULL,
                                    Date_Created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                    Date_Removed DATETIME);''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS Sales (
                                    SaleID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    UserID INTEGER NOT NULL,
                                    TotalAmount REAL NOT NULL,
                                    Date TEXT NOT NULL,
                                    Date_Canceled DATETIME,
                                    Status TEXT NOT NULL,
                                    FOREIGN KEY (UserID) REFERENCES Users (UserID));''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS Transactions (
                                    TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    SaleID INTEGER NOT NULL,
                                    PaymentMethod TEXT NOT NULL,
                                    Amount REAL NOT NULL,
                                    Date TEXT NOT NULL,
                                    Date_Canceled DATETIME,
                                    Status TEXT NOT NULL,
                                    FOREIGN KEY (SaleID) REFERENCES Sales (SaleID));''')

    # Section for table population
    def create_product(self, name, price, quantity, type):
        try:
            self.product_manager.create_product(name, price, quantity, type)
        except sqlite3.IntegrityError as e:
            return 'An error occurred when adding the product:\n{}'.format(e)
        return 'Product created'
    
    def create_user(self, username, password, role):
        try:
            self.user_manager.create_user(username, password, role)
        except sqlite3.IntegrityError as e:
            return 'An error occurred when adding the user:\n{}'.format(e)
        return 'User created'
    
    def create_sale(self, user_id, total_amount, date):
        try:
            self.sales_manager.create_sale(user_id, total_amount, date)
        except sqlite3.IntegrityError as e:
            return 'An error occurred when adding the sale:\n{}'.format(e)
        return 'Sale created'
    
    def create_transaction(self, sale_id, payment_method, amount, date):
        try:
            self.transaction_manager.create_transaction(sale_id, payment_method, amount, date)
        except sqlite3.IntegrityError as e:
            return 'An error occurred when adding the transaction:\n{}'.format(e)
        return 'Transaction created'

    # End of table population section

    # Section for table retrieval
    def get_all_products(self):
        try:
            return self.product_manager.get_all_products()
        except sqlite3.Error as e:
            return 'An error occurred when retrieving the products:\n{}'.format(e)
    
    def get_products(self, name):
        try:
            return self.product_manager.get_products_by_name(name)
        except sqlite3.Error as e:
            return 'An error occurred when retrieving the product:\n{}'.format(e)

    # End of table retrieval section

    def close(self):
        self.conn.close()
