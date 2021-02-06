from kivymd.material_resources import dp

from models.medicamentos import Medicamento
from models.produtos import Produto


class FrentedeLoja:
    def __init__(self):
        self._observers = []
        self._produto = Produto()
        self._medicamento = Medicamento()

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
                ('Código', dp(30)), ('Nome', dp(40)), ('Princípio', dp(50)),
                ('Laboratório', dp(30)), ('Preço', dp(30)),
                ('Quantidade', dp(30)), ('Tarja', dp(30)),
                ('validade', dp(40))
            ],

            'Produtos': [
                ('codigo', dp(30)), ('nome', dp(40)), ('descricao', dp(50)),
                ('quantidade', dp(20)), ('unidadequantidade', dp(20)),
                ('estoque', dp(20)), ('preco', dp(30)), ('validade', dp(40)),
                ('tipo', dp(30))
            ]
        }
        return column_datas[type]

    def query(self, type, text=None):
        if type == 'Medicamentos':
            print('vou pesquisar por:', text)
            return self._medicamento.find_record(text)
        elif type == 'Produtos':
            pass
        elif type == 'all':
            print('pesquisando tudo')
            return self._medicamento.get_all()
