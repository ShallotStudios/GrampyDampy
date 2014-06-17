import pygame.mixer
pygame.mixer.init()

from os import listdir
sound_names = listdir("Sounds\\Effects\\")

sounds = {}
for sn in sound_names :
    sounds[sn] = pygame.mixer.Sound("Sounds\\Effects\\" + sn)

def play(sound_name) :
    sounds[sound_name].play()

def stop(sound_name) :
    sounds[sound_name].stop()

def fadeout(sound_name) :
    sounds[sound_name].fadeout()
