from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import TwoLineListItem

from kivymd.uix.label import MDLabel

class ItemList(MDGridLayout):
    rows = 1
    def __init__(self, **kwargs):
        super(ItemList, self).__init__()

        #need left float layout
        left = MDFloatLayout()
        left_list = TwoLineListItem(text=kwargs['name'], secondary_text='Expiration Date:' + kwargs['exp_date'], pos_hint={"top":.5})
        # left_label = MDLabel(text=kwargs['name'], size_hint=(1, .2), pos_hint={"top": .2, "left": 1})
        left.add_widget(left_list)
        # words.add_widget(left_label)

        self.add_widget(left)