'''
Created on Feb 24, 2017

@author: Robert
'''

import parameters as PRAM


class SolidBackground():
    def __init__(self, color = PRAM.COLOR_BLACK):
        self.color=color
        
    def colorChange(self,color):
        self.color=color
        return True 
        
class StaticSprite():
    def __init__(self, image, location):
        self.image = image
        self.location = location