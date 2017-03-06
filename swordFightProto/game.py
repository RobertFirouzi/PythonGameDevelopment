'''
Created on Mar 4, 2017

@author: Robert
'''

import parameters as PRAM
import sys, importlib
from game_level import GameLevel, GameCutscene, GameMenu
from event import EventLoadMenu

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
                 gameScene = None, ):
        self.player = player
        self.gameScene = gameScene
        self.musicPlayer = musicPlayer
        self.soundPlayer = soundPlayer
        self.renderer = renderer
        self.gameEvents = gameEvents
        self.keydownEvents = keydownEvents
        self.keysPressed =  keysPressed
        self.inputHandler = inputHandler
        self.eventHandler = eventHandler

    '''
    Run at Game() initialization to setup the starting point
    '''
    def gameStartup(self):
        self.addEvent(EventLoadMenu(PRAM.MENU_TEST1))
#         self.addEvent(EventLoadLevel(PRAM.LEV_TEST1))
    
    '''
    Imports the level based on filename and initializes the fields in the 
        gameLevel object.  Loads the game events from the level to be 
        immediately run
    @param levelFile
    '''
    def loadLevel(self, levelFile):
        self.unloadScene() 
        sys.path.append(PRAM.LEVEL_PATH)
        level = importlib.import_module(levelFile)                       
        sys.path.pop()
        
        self.gameScene = GameLevel(
            level.actors,
            level.scenery,
            level.levelEvents,
            level.gameEvents,
            level.layout)

        for event in self.gameScene.gameEvents:
            self.addEvent(event)
            
        self.player.actor = self.gameScene.actors[0] #for now convention is for actor[0] to default to player    
    
    def loadMenu(self, menuFile):
        self.unloadScene()
        sys.path.append(PRAM.MENU_PATH)
        menu = importlib.import_module(menuFile)
        sys.path.pop()
        
        self.gameScene = GameMenu(
            [], #actors
            menu.scenery,
            [], #levelEvents
            menu.gameEvents,
            menu.layout)

        for event in self.gameScene.gameEvents:
            self.addEvent(event)

    def loadCutscene(self, cutsceneFile): #TODO - everything about this
        self.unloadScene()
        sys.path.append(PRAM.MENU_PATH)
        cutscene = importlib.import_module(cutsceneFile)
        sys.path.pop()
        
        self.gameScene = GameCutscene(cutscene) 
    
    '''
    Halt any running events, unload any assets, etc
    ''' 
    def unloadScene(self):
        self.soundPlayer.stopSound()
        self.musicPlayer.stopSong()
        
    def addEvent(self,event):
        self.gameEvents.append(event)
    
    