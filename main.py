from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.audio_list_screen import AudioListScreen
from screens.create_audio_screen import CreateAudioScreen
from screens.welcome_screen import WelcomeScreen

class AudioApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome_screen'))
        sm.add_widget(CreateAudioScreen(name='input_screen'))
        sm.add_widget(AudioListScreen(name='audio_list_screen'))
        return sm

if __name__ == '__main__':
    AudioApp().run()
