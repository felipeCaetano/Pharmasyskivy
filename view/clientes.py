import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

from infrastructure.observer import Observer

from view.barra_voltar import BarraVoltar

Builder.load_file(os.path.join(os.path.dirname(__file__), "clientes.kv"))


class ClientesView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model.add_observer(self)

    def on_save(self, instance):
        self.controller.on_save(instance)

    def on_cancel(self):
        print('cancel')

    def model_is_changed(self):
        print('Salvo com sucesso')
