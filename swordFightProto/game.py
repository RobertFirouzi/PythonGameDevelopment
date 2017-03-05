'''
Created on Mar 4, 2017

@author: Robert
'''

import parameters as PRAM
import sys, importlib
from game_level import GameLevel
from event import EventLoadLevel

'''
The highest level object which contains references to the game level and
    all of the game engine objects
@param player
@param musicPlayer
@param soundPlayer
@param renderer
@param gameEvents
@param eventHandler
@param gameLevel
'''
class Game():
    def __init__(self, 
                 player = None,
                 musicPlayer = None, 
                 soundPlayer = None, 
                 renderer = None,
                 gameEvents = [],
                 keydownEvents = [],
                 keysPressed = [],
                 inputHandler = None,
                 eventHandler = None,
                 gameLevel = None, ):
        self.player = player
        self.gameLevel = gameLevel
        self.musicPlayer = musicPlayer
        self.soundPlayer = soundPlayer
        self.renderer = renderer
        self.gameEvents = gameEvents
        self.keydownEvents = keydownEvents
        self.keysPressed =  keysPressed
        self.inputHandler = inputHandler
        self.eventHandler = eventHandler
        self.gameLevel = gameLevel
        
        self.gameStartup() #load initial settings

    '''
    Run at Game() initialization to setup the starting point
    '''
    def gameStartup(self):
        self.gameEvents.append(EventLoadLevel(PRAM.LEV_TEST1))
    
    '''
    Imports the level based on filename and initializes the fields in the 
        gameLevel object.  Loads the game events from the level to be 
        immediately run
    @param levelFile
    '''
    def initializeLevel(self, levelFile):
        sys.path.append(PRAM.LEVEL_PATH)
        level = importlib.import_module(levelFile)                       
        sys.path.pop()
        
        self.gameLevel = GameLevel(
            level.actors,
            level.scenery,
            level.levelEvents,
            level.gameEvents,
            level.layout)

        for event in self.gameLevel.gameEvents:
            self.addEvent(event)
            
        self.player.actor=self.gameLevel.actors[0] #for now convention is for actor[0] to default to player    
    
    def addEvent(self,event):
        self.gameEvents.append(event)
    