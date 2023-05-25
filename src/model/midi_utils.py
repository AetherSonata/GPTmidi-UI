import pygame

def play_midi(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait while the MIDI file is playing
    while pygame.mixer.music.get_busy():
        continue

    # Cleanup resources
    pygame.mixer.music.stop()
    pygame.mixer.quit()
