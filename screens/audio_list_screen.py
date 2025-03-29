from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from functools import partial
import os


from utils.file_operations import load_audios, save_audios
from utils.audio_player import play_audio, pause_audio, resume_audio, stop_audio

class AudioListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.scroll_view = ScrollView()
        self.list_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.list_layout.bind(minimum_height=self.list_layout.setter('height'))

        # Изначально обновляем список аудио
        self.update_audio_list()
        self.scroll_view.add_widget(self.list_layout)
        self.layout.add_widget(self.scroll_view)

        # Добавляем глобальные кнопки управления воспроизведением
        button_pause = Button(
            text="Пауза",
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5},
            font_size='16sp',
            on_press=self.pause_audio
        )
        button_resume = Button(
            text="Продолжить",
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5},
            font_size='16sp',
            on_press=self.resume_audio
        )
        button_stop = Button(
            text="Стоп",
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5},
            font_size='16sp',
            on_press=self.stop_audio
        )
        self.layout.add_widget(button_pause)
        self.layout.add_widget(button_resume)
        self.layout.add_widget(button_stop)

        button_back = Button(
            text="Назад",
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5},
            font_size='16sp',
            on_press=self.goto_input
        )
        self.layout.add_widget(button_back)

        self.add_widget(self.layout)

    def on_pre_enter(self):
        print("AudioListScreen: on_pre_enter вызван")
        self.update_audio_list()    

    def on_enter(self):
        print("AudioListScreen: on_enter вызван")
        self.update_audio_list()

    def update_audio_list(self):
        self.list_layout.clear_widgets()
        audios = load_audios()
        for audio in audios:
            item = BoxLayout(size_hint_y=None, height=40)
            label = Label(text=os.path.basename(audio), size_hint_x=0.5)
            button_play = Button(
                text="Воспроизвести",
                size_hint_x=0.25,
                on_press=partial(self.play_audio, audio)
            )
            button_delete = Button(
                text="Удалить",
                size_hint_x=0.25,
                on_press=partial(self.delete_audio, audio)
            )

            item.add_widget(label)
            item.add_widget(button_play)
            item.add_widget(button_delete)
            self.list_layout.add_widget(item)


    def play_audio(self, audio, *args):
        play_audio(audio)

    def pause_audio(self, instance):
        pause_audio()

    def resume_audio(self, instance):
        resume_audio()

    def stop_audio(self, instance):
        stop_audio()

    def delete_audio(self, audio, *args):
        try:
            os.remove(audio)
        except FileNotFoundError:
            print(f'Файл {audio} не найден!')
        # удаление и обнавление
        audios = load_audios()
        if audio in audios:
            audios.remove(audio)
            save_audios(audios)
        self.update_audio_list()

    def goto_input(self, instance):
        self.manager.current = 'input_screen'