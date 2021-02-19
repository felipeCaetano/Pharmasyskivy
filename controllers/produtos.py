from view.produtos import ProdutosView


class ProdutosController:

    def __init__(self, model):
        self.model = model
        self.view = ProdutosView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def on_save(self, fields):
        self.model.codigo = fields[0].text
        self.model.nome = fields[1].text
        self.model.descricao = fields[2].text
        self.model.quantidade = fields[5].text
        self.model.unidadequantidade = fields[6].text
        self.model.estoque = fields[13].text
        self.model.preco = fields[-1].text
        self.model.compra = fields[-2].text
        self.model.validade = fields[7].text
        self.model.tipo = fields[8].text
        status, msg = self.model.add(self.model)

    def text_validator(self, text):
        error, msg = self.model.validate(text)
        return error, msg

    def number_validator(self, text):
        error, msg = self.model.validate_number(text)
        return error, msg

    def float_validator(self, text):
        error, msg, s = self.model.validate_price(text)
        return error, msg, s

    def on_cancel(self):
        pass
