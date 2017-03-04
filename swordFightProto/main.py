'''
Created on Feb 24, 2017

@author: Robert
'''
import pygame
import parameters as PRAM
from setup import soundPlayerFactory,gameLevelFactory, playerFactory, gameFactory
from event import EventHandler
from render import Renderer

### SETUP ###
pygame.init()  # @UndefinedVariable
screen = pygame.display.set_mode((PRAM.DISPLAY_WIDTH, PRAM.DISPLAY_HEIGHT))
CLOCK = pygame.time.Clock() 
DONE = False

### GAME ENGINE ###
gameLevel = gameLevelFactory()
musicPlayer, soundPlayer = soundPlayerFactory()
renderer = Renderer(screen)
player = playerFactory(gameLevel.actors[0])
game = gameFactory(player, gameLevel, musicPlayer, soundPlayer, renderer, [], None)
eventHandler = EventHandler(game)
game.eventHandler=eventHandler


#think where this should be called?  (music/ambiance track should be within gameLevel)
musicPlayer.playSong('saga7-Water')
soundPlayer.playSound('city')
soundPlayer.setSoundVolume('city',0.4)

while not DONE:
        ### CHECK THE EVENT QUEUE ###
        for event in pygame.event.get():         
            if event.type == pygame.QUIT:  # @UndefinedVariable
                DONE = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # @UndefinedVariable 
                game.events.append(player.defaultAction())
                    
        ### CHECK BUTTON PRESSES ###   
        pressed = pygame.key.get_pressed()    
        #DIRECTIONAL               
        if pressed[pygame.K_UP]:  # @UndefinedVariable
            player.actionMove('up')
        if pressed[pygame.K_DOWN]:  # @UndefinedVariable
            player.actionMove('down')
        if pressed[pygame.K_LEFT]:  # @UndefinedVariable
            player.actionMove('left')
        if pressed[pygame.K_RIGHT]:  # @UndefinedVariable
            player.actionMove('right')
        
        ### RUN GENERATED EVENTS ###
        eventHandler.handleEvents()
        
        ### DRAW THE GRAPHICS ###
        renderer.renderScenery(game.gameLevel.scenery)
        renderer.renderActors(game.gameLevel.actors)
        pygame.display.flip()
        CLOCK.tick(60)

#this will only run if the module is run as the main module, not if imported
if __name__ == '__main__':
    pass #nop

