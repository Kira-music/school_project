import os
import threading
import pyttsx3
from kivy.clock import Clock
from functools import partial

class AudioProcessor:
  AUDIO_DIR="storage"

  @staticmethod
  def create_audio_directory():
    if not os.path.exists(AudioProcessor.AUDIO_DIR):
      os.makedirs(AudioProcessor.AUDIO_DIR)

  @staticmethod
  def load_audios():
    return [file for file in os.listdir(AudioProcessor.AUDIO_DIR) if file.endswith('.wav')]
