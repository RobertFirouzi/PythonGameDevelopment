'''
Created on Mar 9, 2017

@author: Robert
'''

import parameters as PRAM

def calcTileFromPix(pixelPos):
    return (pixelPos[0]//PRAM.TILESIZE,pixelPos[1]//PRAM.TILESIZE)