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
    def renderActors(self, actorsWrapper):
        for actor in actorsWrapper.actors:
            self.renderActor(actor, actorsWrapper.actorDict)
        return
    
    '''
    Render all scenery
    @param scenery
    '''
    def renderScenery(self, sceneryWrapper):
        for feature in sceneryWrapper.scenery:
            self.renderFeature(feature, sceneryWrapper.imageDict)
        return
    
    '''
    Render an actor onto the screen.  Contains method to render all game actors
    @param actor
    '''
    def renderActor(self, actor, actorDict):
        if type(actor) is SimpleBox:
            pygame.draw.rect(self.screen, actor.color, 
                             pygame.Rect(actor.x, actor.y, actor.width, actor.height))
        return 
    
    '''
    Render a scenery feature to the screen.  Contains methods to render all 
        scenery features
    @param feature
    '''    
    def renderFeature(self, feature, imageDict):
        if type(feature) is SolidBackground:
            self.screen.fill(feature.color)
        elif type(feature) is StaticSprite:
            self.screen.blit(imageDict[feature.image], feature.location)
        return
