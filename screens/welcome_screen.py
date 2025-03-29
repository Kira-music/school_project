from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Верхняя часть – текст приветствия
        greeting = Label(
            text="Добро пожаловать в наше приложение!\nЗдесь вы можете создавать аудио из текста.",
            font_size='20sp',
            halign='center',
            valign='middle',
            size_hint=(1, 0.7)
        )
        # Чтобы текст корректно переносился по ширине, привяжем text_size к размеру Label
        greeting.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        buttons_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.3), spacing=10)

        button = Button(
            text='Продолжить',
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5},
            font_size='16sp',
            on_press=self.goto_input
        )
        button_exit = Button(
            text='Выход',
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5},
            font_size='16sp',
            on_press=self.exit_app
        )

        buttons_layout.add_widget(button)
        buttons_layout.add_widget(button_exit)
        
        layout.add_widget(greeting)
        layout.add_widget(buttons_layout)
        
        self.add_widget(layout)

    def goto_input(self, instance):
        self.manager.current = 'input_screen'

    def exit_app(self, instance):
        # Динамический импорт, чтобы избежать проблем с порядком загрузки
        from kivy.app import App
        print("Выходим из приложения...")
        App.get_running_app().stop()