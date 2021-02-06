from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.relativelayout import RelativeLayout


class ClickableTextFieldRound(RelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]


class Login(MDScreen):
    def build(self):
        return self

    def do_login(self):
        print("logando")
        print(self.ids.login, self.ids.senha)


class Loginapp(MDApp):
    def build(self):
        return Builder.load_file('login.kv')


if __name__ == '__main__':
    Loginapp().run()
