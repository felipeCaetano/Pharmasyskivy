from kivy.properties import ListProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from functools import partial


class ChoiceGrid(GridLayout):
    names = ListProperty(None)
    dispose = StringProperty()

    def __init__(self, group='group', **kwags):
        super().__init__(cols=2, row_force_default=True,
                         row_default_height=30, **kwags)
        self.active = None
        self._names = None
        self._dispose = None
        self.group = group

    def on_kv_post(self, base_widget):
        self.config(self._names, self.group, self.dispose)

    def on_names(self, instance, values):
        self._names = values

    def on_dispose(self, instance, value):
        self._dispose = str(value)

    def checkbox_active(self, checkbox, value, text):
        if value:
            self.active = text

    def config(self, names, group, dispose):
        if dispose == 'vertical':
            self.cols = 2
            self.create_widget(group, names)

        elif dispose == 'horizontal':
            self.cols = len(names) * 2
            self.create_widget(group, names)
        else:
            raise ValueError(
                f"ChoiceGrid.dispose is set to an invalid option {dispose}."
                f"Must be one of: ['horizontal', 'vertical']")

    def create_widget(self, group, names):
        for name in names:
            label = Label(text=name)
            label.color = (9 / 255, 67 / 255, 8 / 255, 1)
            checkbox = CheckBox(group=group)
            checkbox.color = (109 / 255, 167 / 255, 108 / 255, 1)
            checkbox.bind(
                active=partial(self.checkbox_active, text=label.text)
            )
            self.add_widget(label)
            self.add_widget(checkbox)
