'''
Created on Feb 25, 2017

@author: Robert
'''

from actors import SimpleBox
from scenery import StaticSprite, SolidBackground
import pygame

class Renderer():
    def __init__(self, screen):
        self.screen = screen
    
    def renderActors(self, actors):
        for actor in actors:
            self.renderActor(actor)
        return
    
    def renderScenery(self, scenerey):
        for feature in scenerey:
            self.renderFeature(feature)
        return
    
    def renderActor(self, actor):
        if type(actor) is SimpleBox:
            pygame.draw.rect(self.screen, actor.color, 
                             pygame.Rect(actor.x, actor.y, actor.width, actor.height))
        return 
        
    def renderFeature(self, feature):
        if type(feature) is SolidBackground:
            self.screen.fill(feature.color)
        elif type(feature) is StaticSprite:
            self.screen.blit(feature.image, feature.location)
        return
