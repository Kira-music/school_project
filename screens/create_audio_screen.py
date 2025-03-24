from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from functools import partial
import threading
import pyttsx3
import os

from utils.file_operations import load_audios, save_audios
from utils.create_directory import create_audio_directory

# ввод текста
class CreateAudioScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.text_input = TextInput(hint_text="Введите текст для аудирования", multiline=True)
        button_create = Button(text="Создать аудирование", on_press=self.create_audio)
        button_audio_list = Button(text="Список аудио", on_press=self.goto_audio_list)
        button_back = Button(text="Назад", on_press=self.goto_welcome)

        self.layout.add_widget(self.text_input)
        self.layout.add_widget(button_create)
        self.layout.add_widget(button_audio_list)
        self.layout.add_widget(button_back)

        self.add_widget(self.layout)

    def create_audio(self, instance):
        text = self.text_input.text
        if text:
            threading.Thread(target=self.process_audio, args=(text,), daemon=True).start()

    
    def save_audio(self, instance):
        text = self.text_input.text.strip()
        if text:
            threading.Thread(target=self.process_audio, args=(text,), daemon=True).start()



    def process_audio(self, text):
        try:
            # Патчим NSSpeechDriver: если атрибута _current_text нет, устанавливаем его в пустую строку
            engine = pyttsx3.init(driverName='nsss')
            
            audio_dir = create_audio_directory()
            audios = load_audios()
            audio_file_name = f"audio_{len(audios) + 1}.wav"  # используем формат WAV
            audio_file_path = os.path.join(audio_dir, audio_file_name)
            print("Путь к сохраняемому файлу:", audio_file_path)
            
            # Сохраняем аудио в файл и ожидаем завершения синтеза
            try:
                engine.save_to_file(text, audio_file_path)
                engine.runAndWait()
                print("Синтез речи завершён.")
            except Exception as e:
                print(f"Ошибка при синтезе речи: {e}")
                return

            if os.path.exists(audio_file_path):
                print("Файл успешно сохранён:", audio_file_path)
            else:
                print("Файл не найден после синтеза:", audio_file_path)
            
            audios.append(audio_file_path)
            save_audios(audios)
            Clock.schedule_once(partial(self.update_ui, audio_file_path), 0)
        except Exception as e:
            print(f"Ошибка TTS: {e}")



    def update_ui(self, audio_file_path, *args):
        print(f"Файл {audio_file_path} успешно сохранён.")
        # Переключаемся на экран списка аудиофайлов, где можно будет воспроизвести сохранённое аудио
        self.manager.current = 'audio_list_screen'


    def goto_audio_list(self, instance):
        self.manager.current = 'audio_list_screen'

    def goto_welcome(self, instance):
        self.manager.current = 'welcome_screen'
