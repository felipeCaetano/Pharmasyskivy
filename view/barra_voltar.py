from kivy.lang import Builder
from kivymd.uix.toolbar import MDToolbar

kv = """
<BarraVoltar>:
    md_bg_color: 1, 1, 1, 1
    specific_text_color: 0,0,0,1
    right_action_items: [['arrow-left', lambda x: self.voltar(), 'Voltar']]
"""


class BarraVoltar(MDToolbar):
    def build(self):
        return Builder.load_string(kv)

    def voltar(self):
        pass
