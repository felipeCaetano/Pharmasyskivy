import os
from datetime import date

from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty, ColorProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.screen import MDScreen

from infrastructure.observer import Observer
from models.medicmantosenum import ClasseTerapeutica, UnidadeDosagem, \
    Embalagem, Tarja, FormaFarmaceutica

from view.barra_voltar import BarraVoltar


Builder.load_file(os.path.join(os.path.dirname(__file__),
                               "newmedicamentos.kv"))


class MedicamentosView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_items = {
            'Classe Terapeutica': ClasseTerapeutica.list_names_kivy(),
            'Unidade': UnidadeDosagem.list_names_kivy(),
            'Apresentação': Embalagem.list_names_kivy(),
            'Tarja': Tarja.list_names_kivy(),
            'Forma Farmacêutica': FormaFarmaceutica.list_names_kivy(),
        }
        self.menu_unidade = self.create_dropdown_menu(self.ids.drop_unidade)
        self.menu_tarja = self.create_dropdown_menu(self.ids.drop_tarja)
        self.menu_classe = self.create_dropdown_menu(self.ids.drop_classe)
        self.menu_forma = self.create_dropdown_menu(self.ids.drop_forma)
        self.menu_apresentacao = self.create_dropdown_menu(
            self.ids.drop_apresentacao)

        self.model.add_observer(self)

    def on_save(self, instance):
        self.controller.on_save(instance)

    def on_cancel(self, instance):
        print('cancel')

    def create_dropdown_menu(self, widget_id):
        menu = MDDropdownMenu(
                caller=widget_id.parent,
                items=self.menu_items[widget_id.text][1:],
                width_mult=6,
            )
        menu.bind(on_release=self.menu_callback)
        return menu

    def get_menu_name(self, menu):
        if menu == self.menu_tarja:
            menu_name = Tarja.list_names()[0]
        elif menu == self.menu_forma:
            menu_name = FormaFarmaceutica.list_names()[0]
        elif menu == self.menu_classe:
            menu_name = ClasseTerapeutica.list_names()[0]
        elif menu == self.menu_unidade:
            menu_name = UnidadeDosagem.list_names()[0]
        elif menu == self.menu_apresentacao:
            menu_name = Embalagem.list_names()[0]
        return menu_name

    def menu_callback(self, instance_menu, instance_menu_item):
        label = instance_menu.caller.children[1]
        label.text = self.get_menu_name(instance_menu)
        dropdown = instance_menu.caller.children[0]
        dropdown.text = instance_menu_item.text[0:38]
        instance_menu.dismiss()

    def process_date(self, somedate):
        somedate = somedate.strftime('%d/%m/%Y')
        return str(somedate)

    def get_date(self, somedate):
        texto = self.process_date(somedate)
        self.ids.lbl_validade.text = 'Validade:'
        self.ids.dpd_validade.text = texto

    def show_date_picker(self):
        min_date = date.today()
        date_dialog = MDDatePicker(callback=self.get_date, min_date=min_date)
        date_dialog.open()

    def barra_voltar(self):
        pass

    def model_is_changed(self):
        print('Salvo com sucesso')


class Field(MDBoxLayout):
    pass


class PharmaSysRsdBtn(MDRaisedButton):
    width: NumericProperty(150)
    height: NumericProperty(150)
    md_bg_color = ColorProperty()

