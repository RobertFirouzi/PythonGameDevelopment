'''
Created on Feb 24, 2017

@author: Robert
'''
import pygame
import parameters as PRAM
from setup import soundPlayerFactory, playerFactory
from event import EventHandler
from render import Renderer
from game import Game

### SETUP ###
pygame.init()  # @UndefinedVariable
screen = pygame.display.set_mode((PRAM.DISPLAY_WIDTH, PRAM.DISPLAY_HEIGHT))
CLOCK = pygame.time.Clock() 
DONE = False

### GAME ENGINE ###
musicPlayer, soundPlayer = soundPlayerFactory()
renderer = Renderer(screen)
player = playerFactory()
game = Game(player, musicPlayer, soundPlayer, renderer) #on init, loads an event for gameStartup
eventHandler = EventHandler(game)
game.eventHandler=eventHandler #these objects contain references to each other (Game may not need the handler though)

while not DONE:
        ### CHECK THE EVENT QUEUE ###
        for event in pygame.event.get():         
            if event.type == pygame.QUIT:  # @UndefinedVariable
                DONE = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # @UndefinedVariable 
                game.gameEvents.append(player.defaultAction())
                    
        ### CHECK BUTTON PRESSES ###   
        pressed = pygame.key.get_pressed()    
        #DIRECTIONAL               
            #TODO - should dirrectional events return an event for the queue?
        if pressed[pygame.K_UP]:  # @UndefinedVariable
            player.actionMove('up')
        if pressed[pygame.K_DOWN]:  # @UndefinedVariable
            player.actionMove('down')
        if pressed[pygame.K_LEFT]:  # @UndefinedVariable
            player.actionMove('left')
        if pressed[pygame.K_RIGHT]:  # @UndefinedVariable
            player.actionMove('right')
        
        ### RUN GAME EVENTS ###
        eventHandler.handleEvents()
        
        ### DRAW THE GRAPHICS ###
        renderer.renderScenery(game.gameLevel.scenery) #TODO can make local vars for scenery to tidy up
        renderer.renderActors(game.gameLevel.actors)
        pygame.display.flip()
        CLOCK.tick(60) #60 FPS

#this will only run if the module is run as the main module, not if imported.
if __name__ == '__main__':
    pass #nop

