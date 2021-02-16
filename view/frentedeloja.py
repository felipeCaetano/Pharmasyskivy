import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField

from infrastructure.observer import Observer

Builder.load_file(os.path.join(os.path.dirname(__file__), 'frentedeloja.kv'))


class ClickableTextFieldRound(RelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class FrentedeLojaView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    name = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("ESQUEMA:", dir(self))
        print("ESQUEMA CONTROLLER:", dir(self.controller))
        print("ESQUEMA MODEL:", dir(self.model))
        self.model.add_observer(self)
        menu_items = [{"text": 'Medicamentos'}, {"text": 'Produtos'}]
        self.menu_pesquisa = self.create_dropdown_menu(menu_items)
        self.scr_manager = self.ids.screen_manager
        self.add_screens(self.scr_manager)

    def add_screens(self, screenmanager):
        pass
        # screenmanager.add_widget()

    def create_dropdown_menu(self, menu_items):
        menu = MDDropdownMenu(
            caller=self.ids.campo_texto.ids.menubut,
            items=menu_items,
            width_mult=4,
        )
        menu.bind(on_release=self.menu_callback)
        return menu

    def add_client(self):
        self.scr_manager.current = 'clientes'
        self.scr_manager.get_screen(
            'clientes').text.title = 'Cadastrar Cliente:'

    def edit_client(self):
        self.scr_manager.current = 'clientes'
        self.scr_manager.get_screen('clientes').text.title = 'Editar Cliente:'

    def search_client(self):
        box = BoxLayout(orientation='vertical')
        butons = BoxLayout(spacing='25dp')
        cancelar = MDRaisedButton(text='Cancelar', md_bg_color=[1, 0, .15, 1])
        procurar = MDRaisedButton(text='Pesquisar', md_bg_color=[0, 1, .15, 1])
        box.add_widget(MDTextField(hint_text='Digite o CPF'))
        butons.add_widget(cancelar)
        butons.add_widget(procurar)
        box.add_widget(butons)
        self.add_client_dialog = Popup(
            size_hint=(None, None),
            size=(400, 200),
            title='Pesquisar Cliente:',
            separator_color=[47 / 255, 167 / 255, 212 / 255, 1.],
            background='atlas://data/images/defaulttheme/textinput_disabled',
            content=box,
        )
        self.add_client_dialog.open()

    def open(self):
        self.menu_pesquisa.open()
        self.menu_pesquisa.bind(on_release=self.menu_callback)

    def menu_callback(self, instance_menu, instance_menu_item):
        instance_menu.dismiss()
        self.on_search(instance_menu_item.text)

    def on_search(self, type_search):
        self.controller.on_search(type_search, self.ids.campo_texto.text)

    def model_is_changed(self):
        print('salvo com sucesso!')
