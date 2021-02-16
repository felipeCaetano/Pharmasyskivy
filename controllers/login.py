from view.login import LoginView


class LoginController:
    """
    The Class Controller is the bridge between the model and the view.
    """

    def __init__(self, model):
        self.model = model
        self.view = LoginView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def on_login(self, user, password):
        print(user, password)

    def text_validator(self, text):
        error, msg = self.model.validar_entrada(text)
        return error, msg
