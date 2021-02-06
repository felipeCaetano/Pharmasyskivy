from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField

from view.login import Login

Builder.load_file('login.kv')
Builder.load_file('clientes.kv')


class TelaInicial(MDScreen):
    def build(self):
        tela = Builder.load_file('pharmasys.kv')
        return tela

    def on_relese(self):
        pass

    def rail_open(self):

        if self.ids.rail.rail_state == 'open':
            self.ids.rail.rail_state = 'close'
        else:
            self.ids.rail.rail_state = 'open'

        for item in self.ids.rail.ids.box.children:
            item.width = "185dp"


class LojaScreen(MDScreen):
    data_items = ["Teste", "teste1", "teste2"]

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
        menu_items = [{"text": 'Medicamentos'}, {"text": 'Produtos'}]
        self.menu = MDDropdownMenu(
            caller=self.ids.campo_texto.ids.menubut,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()
        self.menu.bind(on_release=self.menu_callback)

    def menu_callback(self, instance_menu, instance_menu_item):
        if instance_menu_item.text == 'Medicamentos':
            instance_menu.dismiss()
            self.search_medicamento()

    def search_medicamento(self):
        row_data = [("4547845", "Dipirona", "Dipirona Sódica", "Medley",
                     "R$ 1,00", "10", "Nenhuma"),
                    ('', '', '', '', '', '', ''), ]

        if row_data is None:
            self.data_table = MDLabel(
                text='Não há resultados.', font_size=72, bold=True,
                pos_hint={'center_x': .5, 'center_y': .5})
        else:
            self.data_table = MDDataTable(
                size_hint=(.7, .6),
                check=True,
                column_data=[
                    ('Código', dp(30)),
                    ('Nome', dp(40)),
                    ('Princípio', dp(50)),
                    ('Laboratório', dp(30)),
                    ('Preço', dp(30)),
                    ('Quantidade', dp(30)),
                    ('Tarja', dp(30)),
                ],
                row_data=row_data,
                elevation=2,
                rows_num=len(row_data),
            )
        self.ids.table.add_widget(self.data_table)


class PharmaSysApp(MDApp):
    screen_manager = ObjectProperty()

    def build(self):
        return TelaInicial()

    def on_start(self):
        self.login = Login()
        for item in self.root.ids.rail.ids.box.children:
            item.width = "190dp"

    def do_login(self):
        Login.do_login(self.login)


if __name__ == '__main__':
    PharmaSysApp().run()
