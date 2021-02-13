from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class FridgeNotesApp(MDApp):
    def build(self):
        label = MDLabel(text='Welcome to FridgeNotes!', halign='center')
        return label

if __name__ == "__main__":
    FridgeNotesApp().run()