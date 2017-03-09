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
          SimpleBox(PRAM.COLOR_ORANGE, [48,48],[0,0])]

#Background, sprites etc
scenery = [
    SolidBackground(PRAM.COLOR_BLACK),
    SimpleBox(PRAM.COLOR_WHITE, [480,480],[0,0]),
    StaticSprite(PRAM.IMAGE_PATH, PRAM.IMG_BALL, (192,192)),
    StaticSprite(PRAM.IMAGE_PATH, PRAM.IMG_BALL, (192,240)),
    StaticSprite(PRAM.IMAGE_PATH, PRAM.IMG_BALL, (240,192)),
    StaticSprite(PRAM.IMAGE_PATH, PRAM.IMG_BALL, (240,240))
    ]

#events triggered within the level
levelEvents = [
    LevelTriggerTouch(EventLoadMenu(PRAM.MENU_TEST1),(53,53),(-5,-5))
    ]

#added to the gameEvent queue on level initialization - e.g. music and ambiant tracks
gameEvents = [
    EventSong(PRAM.SONG_SAGAWATER),
    EventSound(PRAM.AMB_CITY),
    EventSetInput(PRAM.INPTYPE_NORMAL),
    ] 

#level layout map (structure is WIP)
background = [] #imagery that goes behind all other layers
tilemap_ground = []
tilemap_obstacle = []
tilemap_top = []

'''
bits correspond to True/False for a barrier
    0
 1     2
    3
    
    Note that to make the layout appear as a level, read x/y inversely
    e.g. for tile 2,3, get levelBarriers[3][2]
'''
levelBarriers = ( 
#   X    0        1      2       3       4       5       6       7       8       9       Y   
     (0b0011, 0b0001, 0b0001, 0b0001, 0b0001, 0b0001, 0b0001, 0b0001, 0b0001, 0b0101), # 0 
     
     (0b0010, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0100), # 1
     
     (0b0010, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0100), # 2
     
     (0b0010, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0100), # 3
     
     (0b0010, 0b0000, 0b0000, 0b0000, 0b1111, 0b1111, 0b0000, 0b0000, 0b0000, 0b0100), # 4
     
     (0b0010, 0b0000, 0b0000, 0b0000, 0b1111, 0b1111, 0b0000, 0b0000, 0b0000, 0b0100), # 5
     
     (0b0010, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0100), # 6
     
     (0b0010, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0100), # 7
     
     (0b0010, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0000, 0b0100), # 8
     
     (0b1010, 0b1000, 0b1000, 0b1000, 0b1000, 0b1000, 0b1000, 0b1000, 0b1000, 0b1100),  # 9
    )


layout = []



