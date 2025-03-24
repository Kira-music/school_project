from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Продолжить', on_press=self.goto_input)
        layout.add_widget(button)
        self.add_widget(layout)

    def goto_input(self, instance):
        self.manager.current = 'input_screen'