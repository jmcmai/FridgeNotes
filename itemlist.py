from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.label import Label

class ItemList(GridLayout):

    def __init(self, **kwargs):
        super(ItemList, self).__init__()

        #need words
        words = FloatLayout()
        words_label = Label(text=kwargs['name'], size_hint={1, .2}, pos_hint={"top": .2})
        words.add_widget(words_label)

        self.add_widget(words)