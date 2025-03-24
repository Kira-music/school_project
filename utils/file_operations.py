import json
import os

# загрузка аудирований
def load_audios():
    try:
        if os.path.exists('audios.json'):
            with open('audios.json', 'r') as f:
                return json.load(f)
    except json.JSONDecodeError:
        print("Ошибка загрузки JSON. Используется пустой список.")
    return []

# сохранение аудирований
def save_audios(audios):
    with open('audios.json', 'w') as f:
        json.dump(audios, f)