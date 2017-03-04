'''
Created on Mar 4, 2017

@author: Robert
'''
import unittest
import pygame
import parameters as PRAM
from render import Renderer
from actors import SimpleBox
from scenery import SolidBackground, StaticSprite
class Test(unittest.TestCase):

    def setUp(self):
        pygame.init()  # @UndefinedVariable
        screen = pygame.display.set_mode((PRAM.DISPLAY_WIDTH, PRAM.DISPLAY_HEIGHT))
        self.renderer = Renderer(screen)
        
        self.actors = [SimpleBox(),
                       SimpleBox(PRAM.COLOR_BLACK), 
                       SimpleBox(PRAM.COLOR_ORANGE, 10, 27, 5, 4)]
        
        self.scenery = [SolidBackground(),
                        SolidBackground(PRAM.COLOR_BLUE),
                        StaticSprite(pygame.image.load(PRAM.IMAGE_PATH+PRAM.IMG_TEST), (20,20)),
                        StaticSprite(pygame.image.load(PRAM.IMAGE_PATH+PRAM.IMG_TEST), (5,2)),
                        StaticSprite(pygame.image.load(PRAM.IMAGE_PATH+PRAM.IMG_TEST))]
        
    def test_renderScenery(self):
        self.renderer.renderScenery(self.scenery)
        pygame.display.flip()
        
    def test_renderActors(self):
        self.renderer.renderActors(self.actors)
        pygame.display.flip()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()