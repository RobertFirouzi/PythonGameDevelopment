'''
Created on Mar 9, 2017

@author: Robert
'''

import parameters as PRAM

def calcTileFromPix(pixelPos):
    return (pixelPos[0]//PRAM.TILESIZE,pixelPos[1]//PRAM.TILESIZE)

def calcCharPix(actor):
    pixel = actor.getPosition()
    size = actor.size
    return [pixel[0] + size[0]//2, pixel[1] + size[1]*2//3]

def calcPixFromTile(tilePos):
    return (tilePos[0]*PRAM.TILESIZE,tilePos[1]*PRAM.TILESIZE)