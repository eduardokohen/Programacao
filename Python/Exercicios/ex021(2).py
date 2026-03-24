import pygame
import time

# Inicializa o mixer de áudio
pygame.mixer.init()

# Carrega o MP3
pygame.mixer.music.load("ex021.mp3")

# Toca a música
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    time.sleep(1)  # espera 1 segundo antes de checar novamente

print("Música finalizada.")