from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel

from view.frentedeloja import FrentedeLojaView


class FrentedeLojaController:

    def __init__(self, model):
        self.model = model
        self.view = FrentedeLojaView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def on_search(self, type, text):
        print(type, text)
        colum_data = self.model.get_column_data(type)
        row_data = list(self.model.query(type, text))
        row_data = row_data.remove(row_data[0])
        print('Achei:', self.model.query(type, text))
        #
        if not row_data:
            data_table = MDLabel(
                text='Não há resultados.', font_size=72, bold=True,
                pos_hint={'center_x': .5, 'center_y': .5})
        else:
            data_table = MDDataTable(
                size_hint=(.7, .6),
                check=True,
                column_data=colum_data,
                row_data=row_data,
                elevation=2,
                rows_num=len(row_data),
            )
        for chld in self.ids.table.children:
            self.ids.table.remove_widget(chld)
        self.ids.table.add_widget(data_table)

    def on_save(self, instance):
        for id in instance.ids:
            if 'txt_' in id:
                print(id, instance.ids[id], instance.ids[id].valor)
            elif 'drop_' in id:
                print(id, instance.ids[id], instance.ids[id].text)
        self.model.add()

    def on_cancel(self):
        pass
