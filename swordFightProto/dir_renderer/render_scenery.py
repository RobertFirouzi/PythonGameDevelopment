'''
Created on Feb 25, 2017

@author: Robert
'''

import sys,os
sys.path.append(os.path.realpath('')+'\\src')
sys.path.append(os.path.realpath('')+'\\dir_scenery')
sys.path.append(os.path.realpath('')+'\\dir_renderer')

from render_base import *  # @UnresolvedImport
from scenery import *
import pygame

#maintains links to the screen and an array of scenery elements to render
class RenderScenery(RenderBase):
    def __init__(self, screen, scenery):
        super(RenderScenery, self).__init__(screen, scenery)
      
    #render an item to the screen
    def renderFeature(self, component):
        if type(component) is SolidBackground:  # @UndefinedVariable
            self.screen.fill(component.color)
        elif type(component) is StaticSprite:  # @UndefinedVariable
            self.screen.blit(component.image, component.location)
        return