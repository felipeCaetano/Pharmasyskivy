import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty, BooleanProperty
from kivymd.uix.screen import MDScreen

from infrastructure.observer import Observer


Builder.load_file(os.path.join(os.path.dirname(__file__), "startscreen.kv"))


class StartScreenView(MDScreen, Observer):
    """
    This Class implements the Widget of the Project
    Its only visual implementation of the state of model class

    Extends the Observer class and overrides the model_changed method
    """

    controller = ObjectProperty()
    model = ObjectProperty()
    auth = BooleanProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model.add_observer(self)
        self.scr_manager = self.ids.screen_manager
        self.scr_manager.add_widget(
            self.controller.logincontroller.get_screen()
        )
        self.scr_manager.add_widget(
            self.controller.frentelojacontroller.get_screen()
        )
        self.scr_manager.add_widget(
            self.controller.clientescontroller.get_screen()
        )
        self.scr_manager.current = 'telalogin'
        self.auth = False


    def model_is_changed(self):
        pass

    def rail_open(self):

        if self.ids.rail.rail_state == 'open':
            self.ids.rail.rail_state = 'close'
        else:
            self.ids.rail.rail_state = 'open'

        for item in self.ids.rail.ids.box.children:
            item.width = "185dp"
