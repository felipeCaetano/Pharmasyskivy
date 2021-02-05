from view.medicamentos import MedicamentosView


class MedicamentosController:

    def __init__(self, model):
        self.model = model
        self.view = MedicamentosView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def on_save(self, instance):
        for id in instance.ids:
            if 'txt_' in id:
                print(id, instance.ids[id], instance.ids[id].valor)
            elif 'drop_' in id:
                print(id, instance.ids[id], instance.ids[id].text)
