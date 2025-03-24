
import sys
import os
import subprocess

def play_audio(audio_path):
    """
    Проигрывает аудиофайл через системные средства.
    """
    if sys.platform.startswith('win'):
        os.startfile(audio_path)
    elif sys.platform.startswith('darwin'):
        subprocess.Popen(["open", audio_path])
    else:
        subprocess.Popen(["xdg-open", audio_path])
