from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(Screen):
    pass

class CreateAccountScreen(Screen):
    pass

class ListScreen(Screen):
    pass


class CreateNewItemScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        return ScreenManagement()

if __name__ == "__main__":
    MainApp().run()