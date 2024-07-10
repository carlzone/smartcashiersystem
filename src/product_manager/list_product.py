from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.graphics import Color, Line

# Load the KV file
Builder.load_file('src/product_manager/list_product.kv')

class ListProduct(Screen, BoxLayout):
    def __init__(self, db_manager, **kwargs):
        super(ListProduct, self).__init__(**kwargs)
        self.db_manager = db_manager

    def on_enter(self):
        super().on_enter()  # Call the super class's on_enter method if it exists
        self.load_products()

    def on_leave(self, *args):
        if hasattr(self, 'ids') and 'product_list' in self.ids:
            self.ids.product_list.clear_widgets()
        return super().on_leave(*args)

    def create_label_with_border(self, text, size_hint_x, color, valign):
        label = Label(text=text, size_hint_x=size_hint_x, color=color, valign=valign)
        with label.canvas.before:
            Color(0, 0, 0, 1)  # Black color for the border
            Line(points=[label.x, label.y, label.x, label.top, label.right, label.top, label.right, label.y], close=True)
        return label

    def load_products(self):
        product_list = self.db_manager.get_all_products()  # Assuming get_all_products is a method in db_manager
        if not product_list:
            self.show_alert('No products found')
        else:
            count = 0
            for product in product_list:
                print(f"Product: {product[1]}, Price: {product[3]}, Quantity: {product[2]}, Type: {product[4]}")
                counter = Label(text=str(count+1), size_hint_x=0.1, color=(0, 0, 0, 1), valign='middle')
                name_label = Label(text=str(product[1]), size_hint_x=0.5, width=100, color=(0, 0, 0, 1), halign='left', valign='middle')
                name_label.bind(size=name_label.setter('text_size'))
                quantity_label = Label(text=f"{product[3]} {product[4]}", size_hint_x=0.2, color=(0, 0, 0, 1), valign='middle')
                price_label = Label(text=f"P{product[2]}", size_hint_x=0.2, color=(0, 0, 0, 1), valign='middle')

                # Add the widgets to the GridLayout
                self.ids.product_list.add_widget(counter)
                self.ids.product_list.add_widget(name_label)
                self.ids.product_list.add_widget(price_label)
                self.ids.product_list.add_widget(quantity_label)
                count += 1

    def on_back(self):
        print("Back button pressed")
        self.manager.current = 'product_screen'

    def on_search_product(self):
        product_name = self.ids.search_product.text
        products = self.db_manager.get_products(product_name)
        if hasattr(self, 'ids') and 'product_list' in self.ids:
            self.ids.product_list.clear_widgets()
            
        if not products:
            self.show_alert('No products found')
            self.load_products()
        else:
            count = 0
            for product in products:
                print(f"Product: {product[1]}, Price: {product[3]}, Quantity: {product[2]}, Type: {product[4]}")
                counter = Label(text=str(count+1), size_hint_x=0.1, color=(0, 0, 0, 1), valign='middle')
                name_label = Label(text=str(product[1]), size_hint_x=0.5, width=100, color=(0, 0, 0, 1), halign='left', valign='middle')
                name_label.bind(size=name_label.setter('text_size'))
                quantity_label = Label(text=f"{product[3]} {product[4]}", size_hint_x=0.2, color=(0, 0, 0, 1), valign='middle')
                price_label = Label(text=f"P{product[2]}", size_hint_x=0.2, color=(0, 0, 0, 1), valign='middle')

                # Add the widgets to the GridLayout
                self.ids.product_list.add_widget(counter)
                self.ids.product_list.add_widget(name_label)
                self.ids.product_list.add_widget(price_label)
                self.ids.product_list.add_widget(quantity_label)
                count += 1



    def show_alert(self, message):
        popup = Popup(title='Alert',
                    content=Label(text=message),
                    size_hint=(None, None), size=(400, 200))
        popup.open()