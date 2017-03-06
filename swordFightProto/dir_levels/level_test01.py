'''
Created on Mar 4, 2017

@author: Robert
'''

#Preliminary outline of a level module - if this can be just a list of refernces without needing to
#create objects that would be better!

import parameters as PRAM
from scenery import SolidBackground, StaticSprite
from actors import SimpleBox
from event import EventSong, EventSound, EventSetInput
import pygame

#The NPC/PC's for the board.  Current convention is for actor[0] to be player char
actors = [SimpleBox()]

#Background, sprites etc
scenery = [
    SolidBackground(PRAM.COLOR_BLACK),
    StaticSprite(pygame.image.load(PRAM.IMAGE_PATH+PRAM.IMG_BALL), (20,20)),
    ]

#events triggered within the level
levelEvents = []

#added to the gameEvent queue on level initialization - e.g. music and ambiant tracks
gameEvents = [
    EventSong(PRAM.SONG_SAGAWATER),
    EventSound(PRAM.AMB_CITY),
    EventSetInput(PRAM.INPTYPE_NORMAL),
    ] 

#level layout map (structure is WIP)
layout = []
