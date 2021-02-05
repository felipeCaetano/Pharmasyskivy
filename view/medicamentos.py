import os
from datetime import date

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.screen import MDScreen

from infrastructure.observer import Observer
from models.medicmantosenum import ClasseTerapeutica, UnidadeDosagem, Embalagem, Tarja, FormaFarmaceutica

from view.barra_voltar import BarraVoltar


Builder.load_file(os.path.join(os.path.dirname(__file__), "medicamentos.kv"))


class MedicamentosView(MDScreen, Observer):
    #texto = StringProperty()
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_items = {
            'Classe Terapeutica': ClasseTerapeutica.list_names_kivy(),
            'Unidade': UnidadeDosagem.list_names_kivy(),
            'Apresentação': Embalagem.list_names_kivy(),
            'Tarja': Tarja.list_names_kivy(),
            'Forma Farmaceutica': FormaFarmaceutica.list_names_kivy(),
        }
        self.menu_unidade = self.create_dropdown_menu(self.ids.drop_unidade)
        self.menu_tarja = self.create_dropdown_menu(self.ids.drop_tarja)
        self.menu_classe = self.create_dropdown_menu(self.ids.drop_classe)
        self.menu_forma = self.create_dropdown_menu(self.ids.drop_forma)
        self.menu_apresentacao = self.create_dropdown_menu(self.ids.drop_apresentacao)

        self.model.add_observer(self)

    def model_is_changed(self):
        print('is changed')

    def on_save(self, instance):
        self.controller.on_save(instance)

    def on_cancel(self, instance):
        print('cancel')

    def create_dropdown_menu(self, widget_id):
        menu = MDDropdownMenu(
            caller=widget_id,
            items=self.menu_items[widget_id.text],
            width_mult=4,
        )
        menu.bind(on_release=self.menu_callback)
        return menu

    def menu_callback(self, instance_menu, instance_menu_item):
        instance_menu.caller.text = instance_menu_item.text
        instance_menu.dismiss()

    def process_date(self, date):
        date = date.strftime('%d/%m/%Y')
        return str(date)

    def get_date(self, date):
        texto = self.process_date(date)
        self.ids._label.text = 'Validade:'
        self.ids._dropdown.text = texto

    def show_date_picker(self):
        min_date = date.today()
        date_dialog = MDDatePicker(callback=self.get_date, min_date=min_date)
        date_dialog.open()


class Field(MDBoxLayout):
    pass


class Select(MDBoxLayout):
    pass

