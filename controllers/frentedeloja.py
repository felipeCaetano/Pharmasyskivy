from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel

from view.frentedeloja import FrentedeLojaView


class FrentedeLojaController:

    def __init__(self, model):
        self.model = model
        self.view = FrentedeLojaView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def on_add_cliente(self):
        # self.scr_manager.current = 'clientes'
        # self.scr_manager.get_screen(
        #     'clientes').text.title = 'Cadastrar Cliente:'
        pass

    def on_search(self, type_search, text):
        colum_data = self.model.get_column_data(type_search)
        response, content = self.model.query(type_search, text)
        print('O conteudo: ', content)
        row_data_fake = []
        if response:
            row_data = tuple([x.get_data() for x in list(content)])
            for _ in row_data[0]:
                row_data_fake.append('')
            row_data_fake = tuple(row_data_fake)

        if not response:
            data_table = MDLabel(
                text='Não há resultados.', font_size=72, bold=True,
                pos_hint={'center_x': .5, 'center_y': .5})
        else:
            data_table = MDDataTable(
                size_hint=(0.7, 0.6),
                use_pagination=True,
                check=True,
                # name column, width column, sorting function column(optional)
                column_data=colum_data,
                row_data=[row_data[0],
                          row_data_fake],
            )
        for chld in self.view.ids.table.children:
            self.view.ids.table.remove_widget(chld)
        self.view.ids.table.add_widget(data_table)

    def on_save(self, instance):
        for component in instance.ids:
            if 'txt_' in component:
                print(component, instance.ids[component],
                      instance.ids[component].valor)
            elif 'drop_' in component:
                print(component, instance.ids[component],
                      instance.ids[component].text)
        self.model.add()

    def on_cancel(self):
        pass
