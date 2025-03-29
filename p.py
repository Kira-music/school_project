from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'system')

class TestApp(App):
    def build(self):
        ti = TextInput(text='Начальный текст', multiline=True)
        ti.focus = True  # сразу даём фокус, чтобы можно было вставлять текст
        return ti

if __name__ == '__main__':
    TestApp().run()