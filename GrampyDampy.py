title = "Grampy Dampy New Build 01"
# Content :
# -
#
# To Be Added :
# -

import pygame, sys
from pygame.locals import *

# settings
startSong = "misc.wav"
startWorld = "test"
camX, camY = 0, 0
movementSpeed = 15
forceOfGravity = 1
camZoom, playrZoom = 40, 40
skyColor = (204,229,255)

class entity(object) :
    def __init__(self, x, y, name) :
        self.x = x
        self.y = y
        self.name = name
        self.textures = TextureSet(name)
    def getDisplayCoords(self, camCoords) :
        x = (self.x - camCoords[0]) * playrZoom + (width/2) - (playrZoom / 2)
        y = height - ((self.y - camCoords[1]) * playrZoom) - (playrZoom * 2)
        return (x,y)

class TextureSet(object) :
    def __init__(self, name) :
        self.name = name
        self.base_standing_frames = []
        self.base_walking_frames = []
        self.adj_standing_frames = []
        self.adj_walking_frames = []
        for frame in range(FPS_COUNT) :
            self.base_standing_frames.append( pygame.image.load("Textures\\" + name + "\\Standing\\" + name + str(frame) + ".png").convert_alpha() )
            self.base_walking_frames.append( pygame.image.load("Textures\\" + name + "\\Walking\\" + name + str(frame) + ".png").convert_alpha() )
            self.adj_standing_frames.append( pygame.transform.scale( self.base_standing_frames[frame], (playrZoom, playrZoom * 2)) )
            self.adj_walking_frames.append( pygame.transform.scale( self.base_walking_frames[frame], (playrZoom, playrZoom * 2)) )
    def getWalkingFrame(self, frame, right) :
        if right :
            return self.adj_walking_frames[frame]
        else :
            return pygame.transform.flip( self.adj_walking_frames[frame], True, False)
    def getStandingFrame(self, frame) :
        return self.adj_standing_frames[frame]
    def updateFrames(self) :
        for frame in range(FPS_COUNT) :
            self.adj_walking_frames[frame] = pygame.transform.scale( self.base_walking_frames[frame], (playrZoom, playrZoom * 2))
            self.adj_standing_frames[frame] = pygame.transform.scale( self.base_standing_frames[frame], (playrZoom, playrZoom * 2))

class world(object) :
    def __init__(self, name) :
        self.name = name

# initial setup
pygame.init()
import SoundHandler
import MusicHandler
import ControllerHandler
print title

# resources
clock = pygame.time.Clock()
width, height = 800, 600
screen = pygame.display.set_mode((width,height), RESIZABLE, 32)
frameCount = 0
FPS_COUNT = 24
left, right = False, False
xMove, yMove = 0, 0
player = entity(0, 0, "Grampy")

MusicHandler.load(startSong)
#MusicHandler.loop()
world = world(startWorld)

while True :
    # animation
    tick = clock.tick()
    frameCount += tick
    tick /= 1000.
    
    # input
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN :
            if event.key == K_a : #LEFT
                left = True
                if xMove == 0 :
                    xMove = -movementSpeed
            elif event.key == K_d : #RIGHT
                right = True
                if xMove == 0 :
                    xMove = movementSpeed
            elif event.key == K_w : #UP
                if yMove == 0 :
                    yMove = 5
        elif event.type == KEYUP :
            if event.key == K_a : #LEFT
                left = False
                if right :
                    xMove = movementSpeed
                else :
                    xMove = 0
            elif event.key == K_d : #RIGHT
                right = False
                if left :
                    xMove = -movementSpeed
                else :
                    xMove = 0
        elif event.type == MOUSEBUTTONDOWN :
            if event.button == 4 : #Scroll Up
                if frameCount - recentlyZoomed >= 3000:
                    leastRecentlyZoomed = frameCount
                recentlyZoomed = frameCount
                if camZoom < 100:
                    camZoom = camZoom + 1
            elif event.button == 5 : #Scroll Down
                if frameCount - recentlyZoomed >= 3000:
                    leastRecentlyZoomed = frameCount
                recentlyZoomed = frameCount
                if camZoom != 30:
                    camZoom = camZoom - 1
        elif event.type == JOYBUTTONDOWN :
            if event.button == 0:
                if yMove == 0 :
                    yMove = 5
        elif event.type == JOYAXISMOTION :
            if event.axis == 0 :
                xMove = movementSpeed * event.value
            elif event.axis == 1 :
                if event.value < -0.9 and yMove == 0:
                    yMove = 5
        elif event.type == VIDEORESIZE :
            width, height = event.w, event.h
            pygame.display.quit()
            screen = pygame.display.set_mode((width, height),RESIZABLE,32)
                    
    # movement
    if player.y > 0:
        yMove = yMove - (forceOfGravity * 0.016)
    player.x += xMove*tick
    player.y += yMove*tick*4.
    if player.y < 0 :
        yMove = 0
        player.y = 0
    
    # display
    pygame.draw.rect(screen, skyColor, Rect((0,0),(width,height)))
    if camZoom != playrZoom :
            playrZoom = camZoom
            player.textures.updateFrames()

    if xMove == 0 :
        screen.blit(player.textures.getStandingFrame(int((frameCount % 1000) / (1000./FPS_COUNT))), player.getDisplayCoords((camX,camY)))
    elif xMove > 0 :
        screen.blit(player.textures.getWalkingFrame(int((frameCount % 1000) / (1000./FPS_COUNT)), True), player.getDisplayCoords((camX,camY)))
    elif xMove < 0 :
        screen.blit(player.textures.getWalkingFrame(int((frameCount % 1000) / (1000./FPS_COUNT)), False), player.getDisplayCoords((camX,camY)))

    pygame.display.update()
