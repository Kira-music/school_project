from kivy.uix.textinput import TextInput
import subprocess

class MyTextInput(TextInput):
    def do_paste(self, *args):
        try:
            pasted_text = subprocess.check_output("pbpaste", universal_newlines=True)
        except Exception as e:
            pasted_text = ""
            print("Ошибка получения текста из pbpaste:", e)
        self.insert_text(pasted_text)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if ('meta' in modifiers or 'command' in modifiers) and keycode[1] == 'v':
            self.do_paste()
            return True
        return super(MyTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)