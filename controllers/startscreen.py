from controllers.clientes import ClientesController
from controllers.frentedeloja import FrentedeLojaController
from controllers.login import LoginController
from view.startscreen import StartScreenView


class StartScreenController:
    """
    The Class Controller is the bridge between the model and the view.

    """
    def __init__(self, model):
        self.model = model
        self.logincontroller = LoginController(self.model.login)
        self.frentelojacontroller = FrentedeLojaController(
            self.model.frenteloja
        )
        self.clientescontroller = ClientesController(self.model.cliente)
        self.view = StartScreenView(controller=self, model=self.model)

    def get_screen(self):
        return self.view
