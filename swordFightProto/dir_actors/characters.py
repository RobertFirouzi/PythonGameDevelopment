'''
Created on Feb 24, 2017

@author: Robert
'''

### LIBRARIES ###
import sys,os
sys.path.append(os.path.realpath('')+'\\dir_params')
sys.path.append(os.path.realpath('')+'\\dir_actors')

### PARAMS ###
from def_colors import *
from def_size import *


class SimpleBox():
    def __init__(self, color = COLOR_BLUE, width = SIMPLE_BOX_WIDTH, # @UndefinedVariable
                 height = SIMPLE_BOX_HEIGHT, x = 0, y = 0): # @UndefinedVariable
        self.color=color
        self.width=width
        self.height=height
        self.x=x
        self.y=y   
        self.moveSpeed = 10
    
    def colorSwap(self):
        if self.color == COLOR_BLUE: # @UndefinedVariable
            self.setColor(COLOR_ORANGE) # @UndefinedVariable
        else:
            self.setColor(COLOR_BLUE) # @UndefinedVariable
        
    def setColor(self,color):
        self.color=color 