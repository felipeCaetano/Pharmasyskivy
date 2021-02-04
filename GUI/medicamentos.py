from datetime import datetime, date

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.screen import MDScreen
from dashboard import BarraVoltar


class Medicamentos(MDScreen):
    texto = StringProperty()

    def process_date(self, date):
        date = date.strftime('%d/%m/%Y')
        return str(date)

    def get_date(self, date):

        self.texto = self.process_date(date)
        self.ids.validade.texto = self.texto

    def show_date_picker(self):
        min_date = date.today()
        date_dialog = MDDatePicker(callback=self.get_date, min_date=min_date)
        date_dialog.open()


class Field(MDBoxLayout):
    pass

class MedicamentosApp(MDApp):
    def build(self):
        return Medicamentos()


if __name__ == '__main__':
    MedicamentosApp().run()
