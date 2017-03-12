'''
Created on Mar 12, 2017

@author: Robert
'''
import utility as UTIL
import parameters as PRAM

class GameCamera():
    def __init__(self, position = [0,0], tile = (0,0), offset = (0,0)):
        self.position = position #absolute pixel position of the top left corner of camera
        self.tile = tile #tile position of top left corner of camera
        self.offset = offset  #pixels that camera is offset from the boundry of the tile
    
    def getPosition(self):
        return self.position
    
    def getTile(self):
        return self.tile
        
    def getOffset(self):
        return self.offset    
        
    def setPosition(self, position = [0,0]):
        self.position = position
        self.tile = UTIL.calcTileFromPix(position)
        self.offset = (position[0] - (self.tile[0] *PRAM.TILESIZE), position[1] - (self.tile[1] *PRAM.TILESIZE) )
        
    def adjustPosition(self, xChange, yChange):
        self.setPosition((self.position[0] + xChange, self.position[1] + yChange))
        