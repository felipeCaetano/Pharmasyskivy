from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.menu import RightContent
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.relativelayout import RelativeLayout

from sqlalchemy.orm.exc import UnmappedInstanceError, NoResultFound

from models import pessoas
from models.pessoas import User
import infrastructure.core as db


Builder.load_file('Login.kv')
Builder.load_file('LojaScreen.kv')


class ContentNavigationDrawer(BoxLayout):
    aut = False
    screen_manager = ScreenManager()
    nav_drawer = ObjectProperty()


class Login(MDScreen):

    def do_login(self):
        senha = self.ids.senha.text
        login = self.ids.login.text
        session = db.session
        try:
            result = session.query(User).filter(User.nome == login and User.password == senha).one()
            PharmaSysapp.aut = True
            print(PharmaSysapp.aut)
            self.parent.current = "scr 2"
            session.close()
        except NoResultFound:
            self.not_found()
            session.close()

    def not_found(self):
        self.ids.senha.text = ""
        self.ids.login.text = ""
        self.ids.on_error.text = "Login ou Senha Invalidos!"


class LojaScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.toprintando()


    def menu_callback(self, instance_menu, instance_menu_item):
        print(instance_menu, instance_menu_item)

    def toprintando(self):
        print("ai printei")
        print(self.ids.campo_texto.ids)
        menu_itens = [{"icon": "alpha-m", "text": "Medicamentos"}, {"icon": "alpha-p", "text": "Produtos"}]
        self.menu = MDDropdownMenu(
            caller=self.ids.campo_texto.ids.menubut,
            items=menu_itens,
            width_mult=4,
        )
        self.menu.bind(on_release=self.menu_callback)


class ClickableTextFieldRound(RelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    pass


class PharmaSysapp(MDApp):
    screen_manager = ObjectProperty()

    def build(self):
        screen = Builder.load_file('PharmaSysapp.kv')
        return screen


PharmaSysapp().run()

