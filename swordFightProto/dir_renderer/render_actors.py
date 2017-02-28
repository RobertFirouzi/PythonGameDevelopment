'''
Created on Feb 25, 2017

@author: Robert
'''

import sys,os
sys.path.append(os.path.realpath('')+'\\src')
sys.path.append(os.path.realpath('')+'\\actors')
sys.path.append(os.path.realpath('')+'\\dir_renderer')

from render_base import *  # @UnresolvedImport
from characters import * 
import pygame

#maintains links to the screen and an array of scenery elements to render
class RenderActors(RenderBase):  # @UndefinedVariable
    def __init__(self, screen, scenery):
        super(RenderActors, self).__init__(screen, scenery)
      
    #render an item to the screen
    def renderFeature(self, component):
        if type(component) is SimpleBox:  # @UndefinedVariable
            pygame.draw.rect(self.screen, component.color, 
                             pygame.Rect(component.x, component.y, component.width, component.height ))
        return 