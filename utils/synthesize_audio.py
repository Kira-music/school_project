
def synthesize_audio(text, audio_file_path):
  import pyttsx3
  engine = pyttsx3.init()
  try:
    if hasattr(engine, '_driver'):
      setattr(engine._driver, '_current_text', "" )
  except Exception as e:
      print("Ошибка")
  engine.save_to_file(text, audio_file_path)
  try:
    engine.runAndWait()
  except Exception as e:
      print("Ошибка")
