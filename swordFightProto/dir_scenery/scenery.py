'''
Created on Feb 24, 2017

@author: Robert
'''

### LIBRARIES ###
import sys,os
sys.path.append(os.path.realpath('')+'\\dir_params')

### PARAMS ###
from def_colors import *


class SolidBackground():
    def __init__(self, color = COLOR_BLACK): # @UndefinedVariable
        self.color=color
        
    def colorChange(self,color):
        self.color=color 
        
class StaticSprite():
    def __init__(self, image, location):
        self.image = image
        self.location = location