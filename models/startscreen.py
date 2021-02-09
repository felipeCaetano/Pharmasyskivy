from models.cliente import Cliente
from models.frentedeloja import FrentedeLoja
from models.login import Login


class StartScreen:
    """
    This class implements the logic of aplication
    - Modelo de negócios
    The Model class implements the Design Partner Observer methods.
    """
    def __init__(self):
        self.login = Login()
        self.frenteloja = FrentedeLoja()
        self.cliente = Cliente()
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_all(self):
        for x in self._observers:
            x.model_is_changed()