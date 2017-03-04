'''
Created on Feb 24, 2017

@author: Robert
'''

import parameters as PRAM

'''
Render the entire screen a solid color
@param color
'''
class SolidBackground():
    def __init__(self, color = PRAM.COLOR_BLACK):
        self.color=color
        
    def colorChange(self,color):
        self.color=color
        return True 
'''
Render an image file to a pixel tuple location
@param image
@param location
'''        
class StaticSprite():
    def __init__(self, image, location):
        self.image = image
        self.location = location