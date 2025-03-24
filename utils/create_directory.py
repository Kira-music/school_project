import os

def create_audio_directory():
    AUDIO_DIR="storage"
    if not os.path.exists(AUDIO_DIR):
        os.makedirs(AUDIO_DIR)    
    return AUDIO_DIR
