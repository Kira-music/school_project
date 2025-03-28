import vlc
import sys
import os
import subprocess

# Глобальная переменная для текущего плеера
current_player = None

def play_audio(audio_path):
    global current_player
    # Если уже воспроизводится аудио, останавливаем его
    if current_player is not None:
        current_player.stop()
    current_player = vlc.MediaPlayer(audio_path)
    current_player.play()

def pause_audio():
    global current_player
    if current_player is not None:
        current_player.pause()  # pause() обычно переключает состояние (пауза/продолжить)

def resume_audio():
    global current_player
    if current_player is not None:
        # Если плеер находится в состоянии паузы, повторный вызов play() продолжит воспроизведение
        current_player.play()

def stop_audio():
    global current_player
    if current_player is not None:
        current_player.stop()
        current_player = None

