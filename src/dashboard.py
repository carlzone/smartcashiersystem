from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

# Load the KV file
Builder.load_file('src/dashboard.kv')

class Dashboard(Screen, BoxLayout):

    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

    def on_products(self):
        print("Products button pressed")
        self.manager.current = 'product_screen'

    def on_sales(self):
        print("Sales button pressed")

    def on_reports(self):
        print("Reports button pressed")

    def on_users(self):
        print("Users button pressed")

    def on_report_bug(self):
        print("Report Bug button pressed")

    def on_about_us(self):
        print("About Us button pressed")