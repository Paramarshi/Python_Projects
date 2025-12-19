import pygame
import time

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("P:\\Music\\diet-mountain-dew.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)