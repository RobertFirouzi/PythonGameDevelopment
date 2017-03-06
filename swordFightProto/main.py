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
from input import InputHandler, ButtonMap

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
buttonMap = ButtonMap()
inputHandler = InputHandler(game, player, buttonMap)
eventHandler = EventHandler(game)
game.eventHandler = eventHandler #these objects contain references to each other (Game may not need the handler though)
game.inputHandler = inputHandler
game.gameStartup()

while not DONE:
        for event in pygame.event.get():         
            if event.type == pygame.QUIT:  # @UndefinedVariable
                DONE = True #TODO make this an input that creates a quit event?
            if event.type == pygame.KEYDOWN: # @UndefinedVariable 
                game.keydownEvents.append(event)
            
            game.keysPressed = pygame.key.get_pressed()
        
        inputHandler.handleInputs()
        eventHandler.handleEvents()
        
        renderer.renderScenery(game.gameScene.scenery) #TODO can make local vars for scenery to tidy up
        renderer.renderActors(game.gameScene.actors) #TODO package together in a def renderAll() call
        pygame.display.flip()
        CLOCK.tick(60) #60 FPS

#this will only run if the module is run as the main module, not if imported.
if __name__ == '__main__':
    pass #nop

