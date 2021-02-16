from view.medicamentos import MedicamentosView


class MedicamentosController:

    def __init__(self, model):
        self.model = model
        self.view = MedicamentosView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

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
