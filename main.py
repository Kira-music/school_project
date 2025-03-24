import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from screens.audio_list_screen import AudioListScreen
from screens.create_audio_screen import CreateAudioScreen

# стартовый
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Продолжить', on_press=self.goto_input)
        layout.add_widget(button)
        self.add_widget(layout)

    def goto_input(self, instance):
        self.manager.current = 'input_screen'

class AudioApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome_screen'))
        sm.add_widget(CreateAudioScreen(name='input_screen'))
        sm.add_widget(AudioListScreen(name='audio_list_screen'))
        return sm

if __name__ == '__main__':
    AudioApp().run()
