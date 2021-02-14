from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import ThreeLineAvatarListItem
from kivy.uix.image import Image

from kivymd.uix.label import MDLabel

class ItemList(MDGridLayout):
    rows = 1
    def __init__(self, **kwargs):
        super(ItemList, self).__init__()

        #need left float layout
        left = MDFloatLayout()
        left_list = ThreeLineAvatarListItem(text=kwargs['name'], secondary_text='Expiration Date: ' + kwargs['exp_date'],
                                        tertiary_text='Extra Notes: ' + kwargs['extra_notes'] + ', Quantity: '+ kwargs['quantity'], 
                                        pos_hint={"top":.5})
        left_image = Image(source='icons/foodbag.png', pos_hint={"top":.95, "center_x": .08}, size_hint=(.7, .7))
        left_list.add_widget(left_image)
        left.add_widget(left_list)

        self.add_widget(left)