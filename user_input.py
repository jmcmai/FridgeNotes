# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:08:51 2021

@author: koush
"""
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from helpers import grocery_item_helper
from helpers import expiry_date_helper
from helpers import extra_note_helper
import json
import requests

class DemoApp(MDApp):
    
    url = "https://fridgenotes-f5c47-default-rtdb.firebaseio.com/"
    
    def build(self):
        self.theme_cls.primary_palette="Orange"
        screen = Screen()

        # username = MDTextField(
        #     pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #     size_hint_x=None, width=200)

        button = MDRectangleFlatButton(text='Show', pos_hint={'center_x': 0.5, 'center_y': 0.4}, on_release=self.show_data)
        self.grocery_item = Builder.load_string(grocery_item_helper)
        self.expiry_date = Builder.load_string(expiry_date_helper)
        self.extra_note = Builder.load_string(extra_note_helper)
        screen.add_widget(self.grocery_item)
        screen.add_widget(self.expiry_date)
        screen.add_widget(self.extra_note)
        screen.add_widget(button)
        return screen
    
    def show_data(self, str):
        to_database = json.loads(str)
        requests.show_data(url = self.url, str = to_database)


DemoApp().run()
