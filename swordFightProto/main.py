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
game = Game(player, musicPlayer, soundPlayer, renderer)
inputHandler = InputHandler(game, player, ButtonMap())
eventHandler = EventHandler(game)
game.inputHandler = inputHandler

game.gameStartup()
while not DONE:
        for event in pygame.event.get():         
            if event.type == pygame.QUIT:  # @UndefinedVariable
                DONE = True #TODO make this an input that creates a quit event?
            if event.type == pygame.KEYDOWN: # @UndefinedVariable 
                game.keydownEvents.append(event)
            
        game.keysPressed = pygame.key.get_pressed()
        
        inputHandler.handleInputs() #iterates through the keydown and keypressed events
        eventHandler.handleEvents()
        
        game.render()
        
        #debug helper, draw the tile gridlines
        for i in range(10):
            pygame.draw.line(screen, PRAM.COLOR_BLACK,(0, 48*i), (480, 48*i))
            pygame.draw.line(screen, PRAM.COLOR_BLACK,(48*i, 0), (48*i, 480))
        
        pygame.display.flip()
        CLOCK.tick(60) #60 FPS

#this will only run if the module is run as the main module, not if imported.
if __name__ == '__main__':
    pass #nop

