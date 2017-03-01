'''
Created on Feb 25, 2017

@author: Robert
'''

from actors import SimpleBox
from scenery import StaticSprite, SolidBackground
import pygame

#base class to be extended 
class RenderBase():
    def __init__(self, screen, components=[]):
        self.screen = screen
        self.components = components
       
    #iterate through every component
    def render(self):
        for component in self.components:
            self.renderFeature(component)
    
    #define this in the subclass
    def renderFeature(self, component):
        pass 

#maintains links to the screen and an array of scenery elements to render
class RenderActors(RenderBase):
    def __init__(self, screen, actors=[]):
        super(RenderActors, self).__init__(screen, actors)
      
    #render an item to the screen
    def renderFeature(self, component):
        if type(component) is SimpleBox:
            pygame.draw.rect(self.screen, component.color, 
                             pygame.Rect(component.x, component.y, component.width, component.height ))
        return 
    
#maintains links to the screen and an array of scenery elements to render
class RenderScenery(RenderBase):
    def __init__(self, screen, scenery=[]):
        super(RenderScenery, self).__init__(screen, scenery)
      
    #render an item to the screen
    def renderFeature(self, component):
        if type(component) is SolidBackground:
            self.screen.fill(component.color)
        elif type(component) is StaticSprite:
            self.screen.blit(component.image, component.location)
        return