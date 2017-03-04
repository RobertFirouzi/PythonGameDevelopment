'''
Created on Feb 25, 2017

@author: Robert
'''

from actors import SimpleBox
from scenery import StaticSprite, SolidBackground
import pygame

'''
Class which renders images to the screen
@param screen
'''
class Renderer():
    def __init__(self, screen):
        self.screen = screen
    
    '''
    Render all actors
    @param actors
    '''
    def renderActors(self, actors):
        for actor in actors:
            self.renderActor(actor)
        return
    
    '''
    Render all scenery
    @param scenery
    '''
    def renderScenery(self, scenery):
        for feature in scenery:
            self.renderFeature(feature)
        return
    
    '''
    Render an actor onto the screen.  Contains method to render all game actors
    @param actor
    '''
    def renderActor(self, actor):
        if type(actor) is SimpleBox:
            pygame.draw.rect(self.screen, actor.color, 
                             pygame.Rect(actor.x, actor.y, actor.width, actor.height))
        return 
    
    '''
    Render a scenery feature to the screen.  Contains methods to render all 
        scenery features
    @param feature
    '''    
    def renderFeature(self, feature):
        if type(feature) is SolidBackground:
            self.screen.fill(feature.color)
        elif type(feature) is StaticSprite:
            self.screen.blit(feature.image, feature.location)
        return
