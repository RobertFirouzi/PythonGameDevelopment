'''
Created on Mar 4, 2017

@author: Robert
'''

#Preliminary outline of a level module - if this can be just a list of refernces without needing to
#create objects that would be better!

import parameters as PRAM
from scenery import SolidBackground, StaticSprite
from actors import SimpleBox
from event import EventSong, EventSound, EventSetInput, EventLoadMenu, EventLoadLevel
from game_level import LevelTile, LevelEvent

#The NPC/PC's for the board.  Current convention is for actor[0] to be player char
actors = [SimpleBox(PRAM.COLOR_ORANGE, [48,48],[0,0])]

#Background, sprites etc
scenery = [
    SolidBackground(PRAM.COLOR_BLACK),
    SimpleBox(PRAM.COLOR_WHITE, [480,480],[0,0]),
#     StaticSprite(PRAM.IMAGE_PATH, PRAM.IMG_BALL, (192,192)),
#     StaticSprite(PRAM.IMAGE_PATH, PRAM.IMG_BALL, (192,240)),
#     StaticSprite(PRAM.IMAGE_PATH, PRAM.IMG_BALL, (240,192)),
#     StaticSprite(PRAM.IMAGE_PATH, PRAM.IMG_BALL, (240,240))
    ]

#events triggered within the level
levelEvents = [
#     LevelTriggerTouch(EventLoadMenu(PRAM.MENU_TEST1),(53,53),(-5,-5))
    ]

#added to the gameEvent queue on level initialization - e.g. music and ambiant tracks
gameEvents = [
    EventSong(PRAM.SONG_SAGAWATER),
    EventSound(PRAM.AMB_CITY),
    EventSetInput(PRAM.INPTYPE_NORMAL),
    ] 

#level layout map (structure is WIP)
tileDict = {
    'grass' : PRAM.TILE_PATH + 'tile_grass.bmp',
    'rock' : PRAM.TILE_PATH + 'tile_rock.bmp',
    'tree' : PRAM.TILE_PATH + 'tile_tree.bmp'
    }
loadMenu_test1 = LevelEvent(PRAM.TRIG_TOUCH, EventLoadMenu(PRAM.MENU_TEST1))
loadLevel_test2 = LevelEvent(PRAM.TRIG_TOUCH, EventLoadLevel(PRAM.LEV_TEST2, [50,192]))

'''
bits correspond to True/False for a barrier
    0
 1     2
    3
    
    Note that to make the layout appear as a level, read x/y inversely
    e.g. for tile 2,3, get levelBarriers[3][2]
'''
layout = (  
     (LevelTile('grass','','',0b0011,None), LevelTile('grass','','',0b0001,None), LevelTile('grass','','',0b0001,None), LevelTile('grass','','',0b0001,None), LevelTile('grass','','',0b0001,None), 
      LevelTile('grass','','',0b0001,None), LevelTile('grass','','',0b0001,None), LevelTile('grass','','',0b0001,None), LevelTile('grass','','',0b0001,None), LevelTile('grass','','',0b0101,None)),  
     
     (LevelTile('grass','','',0b0010,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), 
      LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0100,None)),
     
     (LevelTile('grass','','',0b0010,loadMenu_test1), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','rock','tree',0b0000,None), 
      LevelTile('grass','rock','tree',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0100,None)),
     
     (LevelTile('grass','','',0b0010,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','rock','tree',0b0000,None), 
      LevelTile('grass','rock','tree',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0100,loadLevel_test2)),
     
     (LevelTile('grass','','',0b0010,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','rock','',0b1111,None), 
      LevelTile('grass','rock','',0b1111,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0100,loadLevel_test2)),
     
     (LevelTile('grass','','',0b0010,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','rock','',0b1111,None), 
      LevelTile('grass','rock','',0b1111,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0100,None)),
     
     (LevelTile('grass','','',0b0010,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), 
      LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0100,None)),
     
     (LevelTile('grass','','',0b0010,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), 
      LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0100,None)),
     
     (LevelTile('grass','','',0b0010,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), 
      LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0000,None), LevelTile('grass','','',0b0100,None)),
     
     (LevelTile('grass','','',0b1010,None), LevelTile('grass','','',0b1000,None), LevelTile('grass','','',0b1000,None), LevelTile('grass','','',0b1000,None), LevelTile('grass','','',0b1000,None), 
      LevelTile('grass','','',0b1000,None), LevelTile('grass','','',0b1000,None), LevelTile('grass','','',0b1000,None), LevelTile('grass','','',0b1000,None), LevelTile('grass','','',0b1100,None)))