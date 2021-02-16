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
from models.medicmantosenum import Embalagem, FormaFarmaceutica
from models.produtosenum import UnidadeVolume, Produtos
from view.barra_voltar import BarraVoltar

Builder.load_file(os.path.join(os.path.dirname(__file__), "produtos.kv"))


class Field(MDBoxLayout):
    on_text_validate = ObjectProperty()


class PharmaSysRsdBtn(MDRaisedButton):
    width: NumericProperty(150)
    height: NumericProperty(150)
    md_bg_color = ColorProperty()


class ProdutosView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_items = {
            'Unidade': UnidadeVolume.list_names_kivy(),
            'Embalagem': Embalagem.list_names_kivy(),
            'Seção': Produtos.list_names_kivy(),
            'Apresentação': FormaFarmaceutica.list_names_kivy(),
        }
        self.menu_unidade = self.create_dropdown_menu(self.ids.drop_unidade)
        self.menu_secao = self.create_dropdown_menu(self.ids.drop_secao)
        self.menu_forma = self.create_dropdown_menu(self.ids.drop_forma)
        self.menu_embalagem = self.create_dropdown_menu(
            self.ids.drop_embalagem)

        self.model.add_observer(self)

    def create_dropdown_menu(self, caller):
        menu = MDDropdownMenu(
            caller=caller,
            items=self.menu_items[caller.text][1:],
            width_mult=6,
        )
        menu.bind(on_release=self.menu_callback)
        return menu

    def menu_callback(self, instance_menu, instance_menu_item):
        label = instance_menu.caller.parent.children[1]
        dropdown = instance_menu.caller.parent.children[0]
        label.text = dropdown.name
        dropdown.text = instance_menu_item.text[0:38]
        instance_menu.dismiss()

    def on_save(self):
        save_list = []
        for component in self.ids:
            if isinstance(self.ids[component], MDDropdownMenu) \
                    or isinstance(self.ids[component], Field):
                save_list.append(self.ids[component])
        error, msg, field = self.controller.text_validator(save_list)
        if not error:
            # self.controller.on_save()
            pass
        else:
            self.text_validator(field, msg)

    def text_validator(self, instance, text):
        print('chamou chamou')
        error, helper_text = self.controller.text_validator(text)
        print(error, helper_text)
        if error:
            print('deu errado')
            instance.error = error
            instance.helper_text = helper_text
        else:
            instance.error = False
            instance.helper_text = helper_text

    def on_cancel(self, instance):
        print('cancel')

    def set_error_message(self, instance, msg):
        instance.error = True
        instance.helper_text = msg

    def process_date(self, date):
        date = date.strftime('%d/%m/%Y')
        return str(date)

    def get_date(self, date):
        texto = self.process_date(date)
        self.ids.lbl_validade.text = 'Validade:'
        self.ids.drop_validade.text = texto

    def show_date_picker(self):
        min_date = date.today()
        date_dialog = MDDatePicker(callback=self.get_date, min_date=min_date)
        date_dialog.open()

    def barra_voltar(self):
        pass

    def model_is_changed(self):
        print('Salvo com sucesso')
