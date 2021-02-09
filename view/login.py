import os

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.relativelayout import RelativeLayout

from infrastructure.observer import Observer

Builder.load_file(os.path.join(os.path.dirname(__file__), "login.kv"))

class ClickableTextFieldRound(RelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]


class LoginView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model.add_observer(self)

    def do_login(self):
        self.controller.on_login(self.ids.login.text, self.ids.senha.text)

    def text_validator(self, instance, text):
        error, helper_text = self.controller.text_validator(text)
        if error:
            instance.error = error
            instance.helper_text = helper_text
        else:
            instance.error = False
            instance.helper_text = helper_text

    def model_is_changed(self):
        pass


class Loginapp(MDApp):
    def build(self):
        return Builder.load_file('login.kv')


if __name__ == '__main__':
    Loginapp().run()
