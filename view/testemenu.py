from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.relativelayout import RelativeLayout

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

KV = '''
<ClickableTextFieldRound>:
    size_hint_y: None
    height: text_field.height
     
    MDTextFieldRound:
        id: text_field
        hint_text: root.hint_text
        text: root.text
        icon_left: 'magnify'
        padding: 20, 20, 20, 20
            # self._lbl_icon_left.texture_size[1] + dp(15) if self.icon_left else dp(25)
     
    MDIconButton:
        id: button
        icon: 'arrow-down-drop-circle-outline'
        ripple_scale: .5
        pos_hint: {"center_y": .5}
        pos: text_field.width -self.width +dp(8), 0
        on_release:
            self.icon = "arrow-down-drop-circle-outline" if self.icon == 'magnify' else 'magnify'
            app.menu.open()
            
Screen:
    name: 'telaloja'
    md_bg_color: [253/255, 253/255, 253/255, 1]
    BoxLayout:
        id: box1
        orientation: 'vertical'
        padding: 50, 20, 20, 20
        
        BoxLayout:
            id: box
            orientation: 'horizontal'
            pos_hint: {"center_x": .5, "center_y":.5}

            ClickableTextFieldRound:
                id: campo_texto
                size_hint_x: None
                width: "500dp"
                hint_text: "Pesquise"
                pos_hint: {"center_x": .5, "center_y":.5}

 
        Widget:
            heigth: 400             



    # MDIconButton:
    #     id: button
    #     icon: "cog"
    #     pos_hint: {"center_x": .5, "center_y": .5}
    #     on_release: app.menu.open()
'''
class ClickableTextFieldRound(RelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [{"text": f"Item {i}"} for i in range(5)]
        print(self.screen.ids.campo_texto.ids)
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.campo_texto.ids.button,
            items=menu_items,
            width_mult=4,
        )
        self.menu.bind(on_release=self.menu_callback)

    def menu_callback(self, instance_menu, instance_menu_item):
        print(instance_menu, instance_menu_item)

    def build(self):
        return self.screen


Test().run()
