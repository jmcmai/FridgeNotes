# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:40:39 2021

@author: koush
"""

grocery_item_helper = """ 
MDTextField:
    hint_text: "Enter Grocery Item"
    helper_text: "or forgot the name of the grocery item"
    helper_text_mode: "on_focus"
    icon_right: "food"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
    size_hint_x: None
    width: 200
    max_text_length: 12
    required: True
    line_color_normal: 1, 1, 0, 1
"""

expiry_date_helper = """ 
MDTextField:
    hint_text: "Enter Expiry Date"
    helper_text: "or forgot the date"
    helper_text_mode: "on_focus"
    icon_right: "calendar-multiple-check"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    size_hint_x: None
    width: 200
    line_color_normal: 2, 1, 0, 1
    required: True
"""


extra_note_helper = """ 
MDTextField:
    hint_text: "some extra note"
    helper_text: "or don't need to add anything"
    helper_text_mode: "on_focus"
    icon_right: "note"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    max_length: 50
    width: 200
    line_color_normal: 7, 1, 0, 1
"""