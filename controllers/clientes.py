from view.clientes import ClientesView


class ClientesController:
    def __init__(self, model):
        self.model = model
        self.view = ClientesView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def on_save(self, instance):
        for components in instance.ids:
            if 'txt_' in components:
                print(components, instance.ids[components],
                      instance.ids[components].valor)
            elif 'drop_' in components:
                print(components, instance.ids[components],
                      instance.ids[components].text)
        self.model.add()

    def on_cancel(self):
        pass
