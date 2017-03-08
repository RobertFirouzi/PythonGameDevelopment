'''
Created on Mar 4, 2017

@author: Robert
'''

#Preliminary outline of a level module - if this can be just a list of refernces without needing to
#create objects that would be better!

import parameters as PRAM
from scenery import SolidBackground, StaticSprite
from actors import SimpleBox
from event import EventSong, EventSound, EventSetInput, EventLoadMenu
from game_level import LevelTriggerTouch

#The NPC/PC's for the board.  Current convention is for actor[0] to be player char
actors = [SimpleBox(),
          SimpleBox(PRAM.COLOR_ORANGE, [32,32],[100,416]),
          SimpleBox(PRAM.COLOR_ORANGE, [48,48],[164,400]),
          SimpleBox(PRAM.COLOR_ORANGE, [64,64],[292,384]),]

#Background, sprites etc
scenery = [
    SolidBackground(PRAM.COLOR_BLACK),
    StaticSprite(PRAM.IMAGE_PATH, PRAM.IMG_BALL, (20,20)),
    StaticSprite(PRAM.IMAGE_PATH, PRAM.IMG_BALL, (200,20)),
    StaticSprite(PRAM.IMAGE_PATH, PRAM.IMG_BALL, (20,200))
    ]

#events triggered within the level
levelEvents = [
    LevelTriggerTouch(EventLoadMenu(PRAM.MENU_TEST1),(20,20),(0,0))
    ]

#added to the gameEvent queue on level initialization - e.g. music and ambiant tracks
gameEvents = [
    EventSong(PRAM.SONG_SAGAWATER),
    EventSound(PRAM.AMB_CITY),
    EventSetInput(PRAM.INPTYPE_NORMAL),
    ] 

#level layout map (structure is WIP)
layout = []
