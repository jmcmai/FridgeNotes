from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.picker import MDDatePicker
import requests
import json
from myfirebase import MyFirebase
from datetime import date, datetime
import random
import traceback
from itemlist import ItemList

class LoginScreen(Screen):
    pass

class LoginScreenSuccess(Screen):
    pass

class SignUpScreen(Screen):
    pass

class SignUpScreenSuccess(Screen):
    pass

class ListScreen(Screen):
    pass


class UserInputScreen(Screen):
    pass

class EditItemScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


class MainApp(MDApp):
    date = ''

    def build(self):
        self.my_firebase = MyFirebase()
        self.theme_cls.primary_palette = "Orange"
        return ScreenManagement()
    
    def signed_in(self):
        #get data from database
        data = self.my_firebase.get_database_data(self.local_id)
        print(data)
        #populate fridge data in list screen
        layout = self.root.ids['list_screen'].ids['list_layout']
        for key in data:
            name = data[key]['name']
            exp_date = data[key]['expiration date']
            extra_notes = data[key]['notes']
            quantity = data[key]['quantity']
            I = ItemList(name=name, exp_date=exp_date, extra_notes=extra_notes, quantity=quantity) # creates card
            layout.add_widget(I)

    # date picker for items
    def show_datepicker(self):
        min_date = date.today()
        picker = MDDatePicker(callback=self.get_date, min_date=min_date)
        picker.open()
    
    def get_date(self, date):
        self.date = date.strftime('%Y-%m-%d')
        print(self.date)
        self.root.ids['user_input_screen'].ids['expiry_date'].text = self.date
          
    # gets information from adding items
    def update_database(self):
        self.root.ids['user_input_screen'].ids['expiry_date'].text = "Expiration Date: " + self.date
        grocery_item = self.root.ids['user_input_screen'].ids["grocery_item"].text
        notes = self.root.ids['user_input_screen'].ids["extra_notes"].text
        quantity = self.root.ids['user_input_screen'].ids["quantity"].text
        if grocery_item == '' or notes == '' or quantity == '':
            self.root.ids['user_input_screen'].ids['invalid_items'].text = "Please fill out all fields."
        else:
            update_items = {'name':grocery_item, 'notes':notes, 'quantity':quantity, 'expiration date':self.date}
            self.my_firebase.db.collection(self.local_id).add(update_items)
            layout = self.root.ids['list_screen'].ids['list_layout']
            I = ItemList(name=grocery_item, exp_date=self.date, extra_notes=notes, quantity=quantity) # creates card
            layout.add_widget(I)
            self.root.current = 'list_screen'

if __name__ == "__main__":
    MainApp().run()