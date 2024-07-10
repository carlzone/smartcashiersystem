from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

# Load the KV file
Builder.load_file('src/product_manager/product_manager.kv')

class ProductManager(Screen, BoxLayout):
    def __init__(self, **kwargs):
        super(ProductManager, self).__init__(**kwargs)

    def on_add_product(self):
        print("Add Product button pressed")
        self.manager.current = 'add_product_screen'

    def on_list_product(self):
        print("List Product button pressed")
        self.manager.current = 'list_product_screen'

    def on_update_product(self):
        print("Update Product button pressed")

    def on_remove_product(self):
        print("Remove Product button pressed")

    def on_back(self):
        print("Back button pressed")
        self.manager.current = 'dashboard_screen'