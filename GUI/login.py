from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.relativelayout import RelativeLayout

KV = '''

'''


class ClickableTextFieldRound(RelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]


class Login(MDScreen):
    ...

class Loginapp(MDApp):
    def build(self):
        return Builder.load_file('Login.kv')
        #pass


Loginapp().run()