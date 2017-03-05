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
Render an image file to a pixel tuple location.  This image must be initialized by
    calling pygame.image.load().  e.g:
        StaticSprite(pygame.image.load(PRAM.IMAGE_PATH+PRAM.IMG_BALL), (20,20))]
@param image
@param location
'''        
class StaticSprite():
    def __init__(self, image, location = (0,0)):
        self.image = image
        self.location = location