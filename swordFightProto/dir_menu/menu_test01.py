'''
Created on Mar 6, 2017

@author: Robert
'''

import parameters as PRAM
from scenery import SolidBackground, StaticSprite
from event import EventSong, EventSetInput
import pygame


scenery = [
    SolidBackground(PRAM.COLOR_BLUE),
    StaticSprite(pygame.image.load(PRAM.IMAGE_PATH+PRAM.IMG_BALL), (200,200)),
    ]

#added to the gameEvent queue on level initialization - e.g. music and ambiant tracks
gameEvents = [
    EventSong(PRAM.SONG_SAGAWIND),
    EventSetInput(PRAM.INPTYPE_MENU),
    ]

layout = [] #TODO 