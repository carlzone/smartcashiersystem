from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from data.db_manager import DatabaseHelper
from src.dashboard import Dashboard
from src.product_manager.product_manager import ProductManager
from src.product_manager.add_product import AddProduct
from src.product_manager.list_product import ListProduct

class SmartCashSystem(App):
    def build(self):
        sm = ScreenManager()
        db_manager = DatabaseHelper('data/smart_cash_register.db')
        sm.add_widget(Dashboard(name='dashboard_screen'))
        sm.add_widget(ProductManager(name='product_screen'))
        sm.add_widget(AddProduct(name='add_product_screen', db_manager=db_manager))
        sm.add_widget(ListProduct(name='list_product_screen', db_manager=db_manager))
        return sm
    
if __name__ == '__main__':
    SmartCashSystem().run()