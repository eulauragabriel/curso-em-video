import pygame

pygame.init()
pygame.mixer_music.load(r'C:\Users\LAURA\Documents\github\curso-em-video\agregados\shinunoga-e-wa.mp3')
pygame.mixer_music.play()

#pygame.event.wait()
#código do gustavo guanabara

while pygame.mixer_music.get_busy():
    continue
