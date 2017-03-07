'''
Created on Feb 24, 2017

@author: Robert
'''

import parameters as PRAM

'''
Class contains the dictionary which has the reference to all loaded sprites, and
    the list of scenery items to place.  Sprites are loaded only once to the dictionary
    but can be placed as many times as they appear in the list
'''
class SceneryWrapper():
    def __init__(self, imageDict = {}, scenery = []):
        self.imageDict = imageDict
        self.scenery = scenery

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
Wrapper class for an image file. Contains the path and image name, and location
to place the image
@param image
@param location
'''         
class StaticSprite():
    def __init__(self, path, image, location = (0,0)):
        self.path = path
        self.image = image
        self.location = location