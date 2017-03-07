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
    
    def render(self, sceneryWrapper, actorsWrapper):
        self.renderScenery(sceneryWrapper)
        self.renderActors(actorsWrapper)
            
    '''
    Render all scenery
    @param sceneryWrapper
    '''
    def renderScenery(self, sceneryWrapper):
        for feature in sceneryWrapper.scenery:
            if type(feature) is SolidBackground:
                self.screen.fill(feature.color)
            elif type(feature) is StaticSprite:
                self.screen.blit(sceneryWrapper.imageDict[feature.image], feature.location)
        return
    
    '''
    Render all actors
    @param actors
    '''
    def renderActors(self, actorsWrapper):
        for actor in actorsWrapper.actors:
            if type(actor) is SimpleBox:
                pygame.draw.rect(self.screen, actor.color, 
                                 pygame.Rect(actor.x, actor.y, actor.width, actor.height))
        return