from kivymd.app import MDApp
from kivy.core.window import Window
from controllers.medicamentos import MedicamentosController
from models.medicamentos import Medicamento


class MedicamentosApp(MDApp):

    def __init__(self, **kwargs):
        super(MedicamentosApp, self).__init__(**kwargs)
        self.model = Medicamento()
        self.controller = MedicamentosController(self.model)

    def build(self):
        Window.size = 800, 640
        return self.controller.get_screen()


if __name__ == '__main__':
    MedicamentosApp().run()
