from kivymd.material_resources import dp

from models.cliente import Cliente
from models.medicamentos import Medicamento
from models.produtos import Produto


class FrentedeLoja:
    def __init__(self):
        self._observers = []
        self._produto = Produto()
        self._medicamento = Medicamento()
        self._cliente = Cliente()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_all(self):
        for x in self._observers:
            x.model_is_changed()

    def get_column_data(self, type):
        column_datas = {
            'Medicamentos': [
                ('Código', dp(50)), ('Nome', dp(60)), ('Princípio', dp(80)),
                ('Laboratório', dp(30)), ("Apresentação", dp(30)),
                ('Dosagem', dp(30)), ('Preço', dp(30)),
                ('Quantidade', dp(30)), ('Tarja', dp(30)),
                ('Estoque', dp(40))
            ],

            'Produtos': [
                ('codigo', dp(50)), ('nome', dp(40)), ('descricao', dp(50)),
                ('preco', dp(30)), ('quantidade', dp(50)), ('estoque', dp(20)),
            ]
        }
        return column_datas[type]

    def query(self, type_search, text=None):
        if type_search == 'Medicamentos':
            return self._medicamento.find_record(text)
        elif type_search == 'Produtos':
            return self._produto.find_record(text)
        elif type_search == 'all':
            return self._medicamento.get_all()
