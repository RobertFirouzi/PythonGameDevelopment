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
    def __init__(self, imageDict = {}, scenery = [], background = False):
        self.imageDict = imageDict
        self.scenery = scenery
        self.background = background

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
    def __init__(self, path, image, size, levelSize = (0,0), scrollX = False, scrollY = False):
        self.path = path
        self.image = image
        self.size = size
        self.scrollX = scrollX
        self.scrollY = scrollY
        self.tileSize = (self.size[0]//PRAM.TILESIZE,self.size[1]//PRAM.TILESIZE)
        
        if scrollX:
            self.scrollFactorX = (levelSize[0] * PRAM.TILESIZE - PRAM.DISPLAY_WIDTH) // (self.size[0] - PRAM.DISPLAY_WIDTH)
        else:
            self.scrollFactorX = 1
        if  self.scrollFactorX == 0:  self.scrollFactorX = 1
        
        if scrollY:
            self.scrollFactorY = (levelSize[1] * PRAM.TILESIZE - PRAM.DISPLAY_HEIGHT) // (self.size[1] - PRAM.DISPLAY_HEIGHT)
        else:
            self.scrollFactorY = 1
        if  self.scrollFactorY == 0:  self.scrollFactorY = 1
                
    #based on the camera position and screen tile to render, find the background tile to render    
    def calcTile(self, tileOffset):       
        return (tileOffset[0] % self.tileSize[0], tileOffset[1] % self.tileSize[1])

    def calcBackgroundCrop(self,tile, cameraTile, cameraOffset):
        if self.scrollX:
            x = (cameraTile[0] * PRAM.TILESIZE + cameraOffset[0])//self.scrollFactorX + tile[0]*PRAM.TILESIZE
        else:
            x = ((tile[0] + cameraTile[0]) % self.tileSize[0]) * PRAM.TILESIZE
            
        if self.scrollY:
            y = (cameraTile[1] * PRAM.TILESIZE + cameraOffset[1])//self.scrollFactorY + tile[1]*PRAM.TILESIZE
        else:
            y = ((tile[1] + cameraTile[1]) % self.tileSize[1]) * PRAM.TILESIZE        
    
        return ((x,y))

    def calcBackgroundLocation(self, location, tile):
        if self.scrollX:
            x = tile[0] * PRAM.TILESIZE
        else: 
            x = location[0]

        if self.scrollY:
            y = tile[1] * PRAM.TILESIZE
        else:
            y = location[1]
        
        return((x,y))
            
    
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