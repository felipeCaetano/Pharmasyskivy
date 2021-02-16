from view.produtos import ProdutosView


class ProdutosController:

    def __init__(self, model):
        self.model = model
        self.view = ProdutosView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def on_save(self):
        self.model.add()

    def text_validator(self, text):
        error, msg = self.model.validate(text)
        return error, msg

    def on_cancel(self):
        pass
