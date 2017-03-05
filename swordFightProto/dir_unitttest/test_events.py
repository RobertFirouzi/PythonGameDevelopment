'''
Created on Mar 4, 2017

@author: Robert
'''
import unittest
import pygame
import parameters as PRAM
from setup import soundPlayerFactory, playerFactory
from actors import SimpleBox
from render import Renderer
from game import Game
from event import EventHandler

class Test(unittest.TestCase):


    def setUp(self):
        pygame.init()  # @UndefinedVariable
        screen = pygame.display.set_mode((PRAM.DISPLAY_WIDTH, PRAM.DISPLAY_HEIGHT))
        actor = SimpleBox()
        musicPlayer, soundPlayer = soundPlayerFactory()
        renderer = Renderer(screen)
        player = playerFactory(actor)
        
        #Game will load the events: load level, playSound, playSong
        game = Game(player, musicPlayer, soundPlayer, renderer)
        self.eventHandler = EventHandler(game)
        game.eventHandler=self.eventHandler

    def test_eventHandler(self):
        self.eventHandler.handleEvents()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()