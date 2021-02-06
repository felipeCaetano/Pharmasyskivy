from view.clientes import ClientesView


class ClientesController:
    def __init__(self, model):
        self.model = model
        self.view = ClientesView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def on_save(self, instance):
        for id in instance.ids:
            if 'txt_' in id:
                print(id, instance.ids[id], instance.ids[id].valor)
            elif 'drop_' in id:
                print(id, instance.ids[id], instance.ids[id].text)
        self.model.add()

    def on_cancel(self):
        pass
