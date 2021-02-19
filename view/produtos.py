import os
from datetime import date

from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty, ColorProperty
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField

from infrastructure.observer import Observer
from models.medicmantosenum import Embalagem, FormaFarmaceutica
from models.produtosenum import UnidadeVolume, Produtos

from view.barra_voltar import BarraVoltar

Builder.load_file(os.path.join(os.path.dirname(__file__), "produtos.kv"))


class PharmaSysRsdBtn(MDRaisedButton):
    width: NumericProperty(150)
    height: NumericProperty(150)
    md_bg_color = ColorProperty()


class CampoTexto(MDTextField):
    pass


class ProdutosView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_items = {
            'Unidade': UnidadeVolume.list_names_kivy(),
            'Embalagem': Embalagem.list_names_kivy(),
            'Tipo': Produtos.list_names_kivy(),
            'Apresentação': FormaFarmaceutica.list_names_kivy(),
        }
        self.menu_unidade = self.create_dropdown_menu(self.ids.drop_unidade)
        self.menu_tipo = self.create_dropdown_menu(self.ids.drop_tipo)
        self.menu_forma = self.create_dropdown_menu(self.ids.drop_forma)
        self.menu_embalagem = self.create_dropdown_menu(
            self.ids.drop_embalagem)
        self.dialog = None
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
        instance_menu.caller.parent.children[1].text = \
            instance_menu.caller.name
        instance_menu.caller.text = instance_menu_item.text
        instance_menu.caller.set_item(instance_menu_item.text)
        instance_menu.dismiss()

    def on_cadastrar(self):
        save_list = []
        error_msg = 'Erro ao Cadastrar:'
        for component in self.ids.values():
            if isinstance(component, MDDropDownItem):
                if component.current_item == '':
                    msg = f'{component.name} não selecionado!'
                    self.show_alert_dialog(error_msg, msg)
                    break
                else:
                    save_list.append(component)
            if isinstance(component, MDTextField):
                if component.error:
                    msg = f'O Campo {component.hint_text} não foi preenchido' \
                          f'corretamente! '
                    self.show_alert_dialog(error_msg, msg)
                    break
                else:
                    save_list.append(component)
        else:
            self.controller.on_save(save_list)

    def show_alert_dialog(self, title, msg):
        self.dialog = MDDialog(
            title=title,
            text=msg,
            buttons=[
                MDRaisedButton(
                    text='OK',
                    md_bg_color=(180/255, 183/255, 189/255, 1),
                    on_release=self.dismiss
                ),
            ]
        )
        self.dialog.open()

    def dismiss(self, instance):
        instance.get_parent_window().children[0].dismiss()

    def text_validator(self, instance, text):
        error, helper_text = self.controller.text_validator(text)
        if error:
            instance.error = error
            instance.helper_text = helper_text
        else:
            instance.error = False

    def number_validator(self, instance, text):
        error, helper_text = self.controller.number_validator(text)
        if error:
            instance.error = error
            instance.helper_text = helper_text
        else:
            instance.error = False

    def float_validator(self, instance, text):
        error, helper_text, string = self.controller.float_validator(text)
        if error:
            instance.error = error
            instance.helper_text = helper_text
        else:
            instance.error = False
            instance.text = "$"
            super(MDTextField, instance).insert_text(string, from_undo=True)

    def on_clear(self, instance):
        print('cancel')
        for field in instance.ids.values():
            if isinstance(field, MDDropDownItem):
                field.text = field.name
                field.current_item = ''
            elif isinstance(field, MDTextField):
                field.select_all()
                field.delete_selection()

    def set_error_message(self, instance, msg):
        instance.error = True
        instance.helper_text = msg

    def process_date(self, date):
        date = date.strftime('%d/%m/%Y')
        return str(date)

    def get_date(self, selected_date):
        texto = self.process_date(selected_date)
        self.ids.lbl_validade.text = 'Validade:'
        self.ids.drop_validade.text = texto
        self.ids.drop_validade.set_item(texto)

    def show_date_picker(self):
        min_date = date.today().day
        date_dialog = MDDatePicker(
            title='Selecione a Data',
            day=min_date,
            min_year=2021,
            text_current_color=get_color_from_hex("#e93f39")
        )
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        self.get_date(value)

    def barra_voltar(self):
        pass

    def model_is_changed(self):
        msg = 'Salvo com sucesso'
        title = 'Cadastro:'
        self.show_alert_dialog(title, msg)
