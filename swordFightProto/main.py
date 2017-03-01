'''
Created on Feb 24, 2017

@author: Robert
'''

#TODO 
#    - create init function which takes in the actors, scenery, etc and initializes
#    - wrap main code into a class.  How to organize this?
#    -python Docs *akin java docs)
#    - create unit tests (how to run automatically? - WIP
#        -output bat results to a file (better way to see results?
#   - good error checking and notification (not just a log file!) - WIP
#    -create debug console
#    setup game structure (Level object, etc)
#    countinue with pygame tutorial

### LIBRARIES ###
import pygame
import os

### PARAMS ###
import parameters as PRAM

### ACTORS ###
from actors import SimpleBox
from scenery import SolidBackground, StaticSprite
from actions import ActionColorSwap, ActionMove

### ENGINE ###
from render import RenderActors, RenderScenery
from player_character import PlayerCharacter

### LOGGING ###
from log_errors import logError

### SOUND ###
from sound import SoundEffectPlayer, SoundWrapper, MusicPlayer

### SETUP ###
pygame.init()  # @UndefinedVariable
IMAGE_PATH = os.path.realpath('')+'\\dir_image\\'
MUSIC_PATH = os.path.realpath('')+'\\dir_sound\\dir_music\\'
AMBIENCE_PATH = os.path.realpath('')+'\\dir_sound\\dir_ambience\\'
SOUND_PATH = os.path.realpath('')+'\\dir_sound\\dir_soundeffects\\'
screen = pygame.display.set_mode((PRAM.DISPLAY_WIDTH, PRAM.DISPLAY_HEIGHT))
CLOCK = pygame.time.Clock() 
DONE = False

### ACTORS ###
actors = []
box = SimpleBox()  # @UndefinedVariable
actors.append(box)

### SCENERY ###
scene = []
background = SolidBackground(PRAM.COLOR_BLACK)
#TODO create a load image function
img_ball = StaticSprite(pygame.image.load(IMAGE_PATH+'ball.png'), (20,20))
scene.append(background)
scene.append(img_ball)

### SOUND ###
musicPlayer = MusicPlayer()
musicPlayer.loadSong(SoundWrapper('song', MUSIC_PATH, 'saga7-Wind', '.mp3'))
musicPlayer.loadSong(SoundWrapper('song', MUSIC_PATH, 'saga7-Water', '.mp3'))
musicPlayer.playSong('saga7-Water')

soundPlayer = SoundEffectPlayer()
soundPlayer.loadSound(SoundWrapper('sound', SOUND_PATH, 'click', '.wav'))
soundPlayer.loadSound(SoundWrapper('sound', AMBIENCE_PATH, 'city', '.wav'))
soundPlayer.playSound('city')
soundPlayer.setSoundVolume('city',0.4)

### GAME ENGINE ###
renderActors = RenderActors(screen,actors)
renderScenery = RenderScenery(screen,scene)

### CONTROL ### 
player = PlayerCharacter(box)
actionMove = ActionMove()
defaultAction = ActionColorSwap(['click'],soundPlayer)
player.actionMove=actionMove.act
player.defaultAction=defaultAction.act
    
### PROGRAM START ###
while not DONE:
        ### CHECK THE EVENT QUEUE ###
        for event in pygame.event.get():         
            if event.type == pygame.QUIT:  # @UndefinedVariable
                DONE = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # @UndefinedVariable 
                player.defaultAction(player)
                    
        ### CHECK BUTTON PRESSES ###   
        pressed = pygame.key.get_pressed()    
        #DIRECTIONAL               
        if pressed[pygame.K_UP]:  # @UndefinedVariable
            player.actionMove(player,['up'])
        if pressed[pygame.K_DOWN]:  # @UndefinedVariable
            player.actionMove(player,['down'])
        if pressed[pygame.K_LEFT]:  # @UndefinedVariable
            player.actionMove(player,['left'])
        if pressed[pygame.K_RIGHT]:  # @UndefinedVariable
            player.actionMove(player,['right'])
        
        ### DRAW THE GRAPHICS ###
        renderScenery.render()
        renderActors.render()
        pygame.display.flip()
        CLOCK.tick(60)

### END MAIN LOOP ###

#############################################################################

#this will only run if the module is run as the main module, not if imported
if __name__ == '__main__':
    pass #nop


############################################################################