import pygame

pygame.init()
pygame.mixer_music.load(r'C:\Users\LAURA\Documents\github\curso-em-video\agregados\shinunoga-e-wa.mp3')
pygame.mixer_music.play()

while pygame.mixer_music.get_busy():
    continue
