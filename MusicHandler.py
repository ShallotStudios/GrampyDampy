import pygame.mixer
import thread
from time import sleep
from os import listdir

def changeTo(new_song) :
    try :
        thread.start_new_thread( _changeSng, (new_song,))
    except:
        print "Song starting error."

def _changeSng(new_song) :
    fadeout()
    sleep(6)
    load(new_song)
    play()

def load(new_song) :
    pygame.mixer.music.load("Sounds\\Music\\" + new_song)

def play() :
    pygame.mixer.music.play()

def fadeout() :
    pygame.mixer.music.fadeout(5000)
    
def fadeoutwithtime(time) :
    pygame.mixer.music.fadeout(time)

def stop() :
    pygame.mixer.music.stop()

def loop() :
    pygame.mixer.music.play(-1)
