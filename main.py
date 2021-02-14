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

class ScreenManagement(ScreenManager):
    pass


class MainApp(MDApp):
    refresh_token_file = "refresh_token.txt"
    date = ''

    def build(self):
        self.my_firebase = MyFirebase()
        return ScreenManagement()

    def on_start(self):
        try:
            # Try to read the persistent signin credentials (refresh token)
            with open(self.refresh_token_file, 'r') as f:
                refresh_token = f.read()
            # Use refresh token to get a new idToken
            id_token, local_id = self.my_firebase.exchange_refresh_token(refresh_token)
            self.local_id = local_id
            self.id_token = id_token
            #get data from database
            data = self.my_firebase.get_database_data(self.local_id)
            #populate fridge data in list screen
            layout = self.root.ids['list_screen'].ids['list_layout']
            for key in data:
                name = data[key]['name']
                exp_date = data[key]['expiration date']
                quantity = data[key]['quantity']
                I = ItemList(name=name, exp_date=exp_date) # creates card
                layout.add_widget(I)
        except Exception as e:
            traceback.print_exc()
            pass

    # date picker for items
    def show_datepicker(self):
        min_date = date.today()
        picker = MDDatePicker(callback=self.got_date, min_date=min_date)
        picker.open()
    
    def got_date(self, the_date):
        date = the_date
        self.root.ids['user_input_screen'].ids['expiry_date'].text = "Expiration Date: " + str(date)
        expiry_date = str(date)    

    # gets information from adding items
    def show_item_data(self):
        grocery_item = self.root.ids['user_input_screen'].ids["grocery_item"].text
        notes = self.root.ids['user_input_screen'].ids["extra_notes"].text
        quantity = self.root.ids['user_input_screen'].ids["quantity"].text
        try:
            print(grocery_item, notes, quantity, str(date))
            self.root.current = 'list_screen'
        except:
            print("fill in all parts!")

    #checks user sign-in
    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            print('success!')
            self.root.current = 'list_screen'
            self.root.transition.direction = 'left'
        else:
            self.root.ids['login_screen'].ids['wrong_login'].text = "Wrong username or password!"

    #adds a new user
    def add_user(self, uname, email, pword):
        with open ("users.json") as file:
            users = json.load(file)
        print(users)

        if(uname != '' and email != '' and pword != ''):
            users[uname] = {'username': uname, 'email': email, 'password': pword,
                    'created':datetime.now().strftime("%Y-%m-%D %H-%M-%S")}

            with open("users.json", 'w') as file:
                json.dump(users, file)
            print("success!")
            self.root.current = 'login_screen'
        else:
            self.root.ids['sign_up_screen'].ids['invalid_sign_up'].text = "Please fill in all text boxes."
            print("failed")

if __name__ == "__main__":
    MainApp().run()