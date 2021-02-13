from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.picker import MDDatePicker
import requests
import json
from datetime import date
import random
from itemlist import ItemList

class LoginScreen(Screen):
    # def sign_up(self):
    #     self.manager.current = "sign_up_screen"

    # def login(self, uname, pword):
    #     with open("users.json") as file:
    #         users = json.load(file)
    #     if uname in users and users[uname]['password'] == pword:
    #         self.manager.current = 'login_screen_success'
    #     else:
    #         self.ids.login_wrong.text = "Wrong username or password!"
    pass

class LoginScreenSuccess(Screen):
    def log_out(self):

        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open ("users.json") as file:
            users = json.load(file)
        print(users)

        users[uname] = {'username': uname, 'password': pword,
                'created':datetime.now().strftime("%Y-%m-%D %H-%M-%S")}

        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current = "sign_up_screen_success"
    pass

class SignUpScreenSuccess(Screen):
    def go_to_login(self):

        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class ListScreen(Screen):
    pass


class UserInputScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


class MainApp(MDApp):
    userid = 'user1' #TESTING WITH USER1
    date = ''

    def build(self):
        return ScreenManagement()

    def on_start(self):
        #get database data
        result = requests.get("https://fridgenotes-f5c47-default-rtdb.firebaseio.com/" + str(self.userid) + ".json")
        print("accepted?", result.ok)
        data = json.loads(result.content.decode())
        print(data)
        fridge = data['fridge']
    
        #populate fridge data in list screen

        # layout = self.root.ids['list_screen'].ids['list_layout']
        # for category, items in fridge.items():
        #     category_items = data['fridge'][category]
        #     print("Category: " + category + " Items: ")
        #     for items in category_items[1:]:
        #         I = ItemList(name=items['name']) # creates card
        #         layout.add_widget(I)

                # print(items['name'])
                # print(items['expirydate'])
                # print(items['quantity'])



    # date picker for items
    def show_datepicker(self):
        min_date = date.today()
        picker = MDDatePicker(callback=self.got_date, min_date=min_date)
        picker.open()
    
    def got_date(self, the_date):
        date = the_date
        print(date)    

if __name__ == "__main__":
    MainApp().run()