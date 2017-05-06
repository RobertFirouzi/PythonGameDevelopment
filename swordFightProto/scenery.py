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
    def __init__(self, imageDict = {}, scenery = [], background = False, foreground = False):
        self.imageDict = imageDict
        self.scenery = scenery
        self.background = background
        self.foreground = foreground

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

class BackgroundImage():
    def __init__(self, path, image, size, levelSize = (0,0), visibleSections = [], scrollX = False, scrollY = False, alpha = False):
        self.path = path
        self.image = image
        self.size = size
        self.visibleSections = visibleSections #(left edge, right edge, top edge, bottom edge)
        self.scrollX = scrollX
        self.scrollY = scrollY
        self.alpha = alpha
        
        
        #NOTE: This is the algorithm used to find the scroll speed for an image to perfeclty scroll the entire level with no tiling
        if scrollX:
            denominator = size[0] - PRAM.DISPLAY_WIDTH
            if denominator <=0:
                denominator = 1
            self.scrollFactorX = (levelSize[0] * PRAM.TILESIZE - PRAM.DISPLAY_WIDTH) // denominator
        else:
            self.scrollFactorX = 1
        if  self.scrollFactorX == 0:  self.scrollFactorX = 1
        
        if scrollY:
            denominator = size[1] - PRAM.DISPLAY_HEIGHT
            if denominator <=0:
                denominator = 1            
            self.scrollFactorY = (levelSize[1] * PRAM.TILESIZE - PRAM.DISPLAY_HEIGHT) // denominator
        else:
            self.scrollFactorY = 1
        if  self.scrollFactorY == 0:  self.scrollFactorY = 1

    
    '''
    @param path: directory of image
    @param image: filename of image
    @param imageSize: size in pixels of image [x,y]
    @param visibleSections: 2d array: each array is a box [left edge, right edge, top edge, bottom edge]
    @param scrolling: [[ScrollX?, multiplier, divisor], [scrollY?, multiplier, divisor]]    
    @param: alpha: does the image contain alpha information (e.g. invisiible pixels)
    
    Scroll speed can be calculated to perfectly scroll the level in the level editor, or user chosen. Formula to scroll the level is
    X direction:
    numerator: levelSize - displaywidth
    denomonator: imageSize - displaywidth
    numerator/denomonator = scroll speed in X direction to scroll the image over the entire level
    Y direction is same using Y params and displayheight
    NOTE if imageSize=displayWidth than set scroll speed to 0
    The above calculates the divisor.  Multiplier makes the image scroll faster then the level, so this must be user chosen.
    If user desires a 1.4 scroll speed, choose a multiplier of 14 and divisor of 10.
    '''
class ForegroundImage():
    def __init__(self, path, image, imageSize, visibleSections, scrolling = [[False,1,1],[False,1,1]], alpha = False):
        self.path = path
        self.image = image
        self.imageSize = imageSize
        self.visibleSections = visibleSections
        self.scrolling = scrolling
        self.alpha = alpha

            
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