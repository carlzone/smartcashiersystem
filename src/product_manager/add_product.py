from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder

# Load the KV file
Builder.load_file('src/product_manager/add_product.kv')

class AddProduct(Screen, BoxLayout):
    def __init__(self, db_manager, **kwargs):
        super(AddProduct, self).__init__(**kwargs)
        self.db_manager = db_manager

    def on_back(self):
        print("Back button pressed")
        self.manager.current = 'product_screen'

    def on_store_product(self):
        product_name = self.ids.product_name.text
        product_quantity = self.ids.product_quantity.text
        product_unit = self.ids.unit_spinner.text
        product_price = self.ids.product_price.text
        
        if not product_name or not product_quantity or not product_price:
            self.show_alert('Please fill in all fields')
        else:
            result = self.db_manager.create_product(product_name, product_price, product_quantity, product_unit)
            if 'error' in result.lower():
                self.show_alert(result)
            else:
                print(f"Storing product: {product_name}, Quantity: {product_quantity} {product_unit}, Price: {product_price}")
            
                self.ids.product_name.text = ''
                self.ids.product_quantity.text = ''
                self.ids.product_price.text = ''

                self.show_alert('Product stored successfully')

    def show_alert(self, message):
        popup = Popup(title='Alert',
                    content=Label(text=message),
                    size_hint=(None, None), size=(400, 200))
        popup.open()