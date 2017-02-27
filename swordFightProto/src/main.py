'''
Created on Feb 24, 2017

@author: Robert
'''

#TODO 
#    - create init function which takes in the actors, scenery, etc and initializes
#    - wrap main code into a class
#    - organize image paths into a dictionary
#    - create an array of sound effect names to reference (instead of typing 'click')
#    - push into a GIT repo
#    - solve ambient sound problem

### LIBRARIES ###
import pygame
import sys,os
sys.path.append(os.path.realpath('')+'\\dir_params')
sys.path.append(os.path.realpath('')+'\\dir_actors')
sys.path.append(os.path.realpath('')+'\\dir_scenery')
sys.path.append(os.path.realpath('')+'\\dir_renderer')
sys.path.append(os.path.realpath('')+'\\dir_control')
sys.path.append(os.path.realpath('')+'\\dir_sound')
sys.path.append(os.path.realpath('')+'\\dir_sound\\dir_music')
sys.path.append(os.path.realpath('')+'\\dir_sound\\dir_ambience')
sys.path.append(os.path.realpath('')+'\\dir_sound\\dir_soundeffects')
sys.path.append(os.path.realpath('')+'\\src')

### PARAMS ###
from def_colors import *
from def_size import *

### ACTORS ###
from characters import *
from scenery import *

### ENGINE ###
from render_actors import RenderActors  # @UnresolvedImport
from render_scenery import RenderScenery  # @UnresolvedImport
from player_actions import ActionMove, ActionDefault  # @UnresolvedImport
from player_character import *

### SOUND ###
from sound_player import MusicPlayer, SoundEffectPlayer  # @UnresolvedImport

### SETUP ###
pygame.init()  # @UndefinedVariable
IMAGE_PATH = os.path.realpath('')+'\\dir_image\\'
MUSIC_PATH = os.path.realpath('')+'\\dir_sound\\dir_music\\'
AMBIENCE_PATH = os.path.realpath('')+'\\dir_sound\\dir_ambience\\'
SOUND_PATH = os.path.realpath('')+'\\dir_sound\\dir_soundeffects\\'
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))  # @UndefinedVariable
CLOCK = pygame.time.Clock() 
DONE = False

### ACTORS ###
actors = []
box = SimpleBox()  # @UndefinedVariable
actors.append(box)

### SCENERY ###
scene = []
background = SolidBackground(COLOR_BLACK) # @UndefinedVariable
#TODO create a load image function
img_ball = StaticSprite(pygame.image.load(IMAGE_PATH+'ball.png'), (20,20))  # @UndefinedVariable

scene.append(background)
scene.append(img_ball)

### SOUND ###
playlist_music = []
music_saga7 = MUSIC_PATH+'saga7.mp3'
playlist_music.append(music_saga7)
musicPlayer = MusicPlayer(playlist_music)
musicPlayer.playRepeat()


soundPlayer = SoundEffectPlayer()
soundPlayer.loadSound(SOUND_PATH, 'click', '.wav')
# soundPlayer.loadSound(AMBIENCE_PATH, 'city', '.mp3') # can't play mp3?
# soundPlayer.playSound('city')

### GAME ENGINE ###
renderActors = RenderActors(screen,actors)
renderScenery = RenderScenery(screen,scene)

### CONTROL ### 
player = PlayerCharacter(box)  # @UndefinedVariable
player.defaultAction=player.colorSwap
            
### PROGRAM START ###
while not DONE:
        ### CHECK THE EVENT QUEUE ###
        for event in pygame.event.get():         
            if event.type == pygame.QUIT:  # @UndefinedVariable
                DONE = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # @UndefinedVariable 
                player.performAction(ActionDefault())
                soundPlayer.playSound('click')
                    
        ### CHECK BUTTON PRESSES ###   
        pressed = pygame.key.get_pressed()    
        #DIRECTIONAL               
        if pressed[pygame.K_UP]:  # @UndefinedVariable
            player.performAction(ActionMove('up'))
        if pressed[pygame.K_DOWN]:  # @UndefinedVariable
            player.performAction(ActionMove('down'))
        if pressed[pygame.K_LEFT]:  # @UndefinedVariable
            player.performAction(ActionMove('left'))
        if pressed[pygame.K_RIGHT]:  # @UndefinedVariable
            player.performAction(ActionMove('right'))
        
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
