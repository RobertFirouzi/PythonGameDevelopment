'''
Created on Mar 4, 2017

@author: Robert
'''

import parameters as PRAM
import sys, importlib
from game_level import GameLevel, GameCutscene, GameMenu
from event import EventLoadMenu
from scenery import StaticSprite, SceneryWrapper
from actors import ActorsWrapper
import pygame

'''
The highest level object which contains references to the game level and
    all of the game engine objects
@param player
@param musicPlayer
@param soundPlayer
@param renderer
'''
class Game():
    def __init__(self, player = None, musicPlayer = None, soundPlayer = None, renderer = None):
        self.player = player
        self.musicPlayer = musicPlayer
        self.soundPlayer = soundPlayer
        self.renderer = renderer
        #explicitly name Class fields
        self.gameEvents = []
        self.keydownEvents = []
        self.gameScene = None
        self.inputHandler = None

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
            self.loadActors(level.actors), #returns an actorsWrapper object
            self.loadImages(level.scenery), #returns a sceneryWrapper object
            level.levelEvents,
            level.gameEvents,
            level.layout)
        
        for event in self.gameScene.gameEvents:
            self.addEvent(event)
            
        self.player.actor = self.gameScene.actorsWrapper.actors[0] #for now convention is for actor[0] to default to player    
    
    def loadMenu(self, menuFile):
        self.unloadScene()
        sys.path.append(PRAM.MENU_PATH)
        menu = importlib.import_module(menuFile)
        sys.path.pop()
        
        self.gameScene = GameMenu(
            self.loadActors(menu.actors), #returns an actorWrapper object
            self.loadImages(menu.scenery), #returns a sceneryWrapper object
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

    def loadActors(self, actors):
        actorDict = {}
        for actor in actors:
            if type(actor) is StaticSprite: #TODO this will be type Sprite
                if actorDict.get(actor.image) == None:
                    actorDict[actor.image] = pygame.image.load(actor.path+actor.image).convert()
                    
        return ActorsWrapper(actorDict, actors)

    def loadImages(self, scenery):
        imageDict = {}
        for sprite in scenery:
            if type(sprite) is StaticSprite:
                if imageDict.get(sprite.image) == None:
                    imageDict[sprite.image] = pygame.image.load(sprite.path+sprite.image).convert()
                    
        return SceneryWrapper(imageDict, scenery)
       
    def render(self):
        self.renderer.render(self.gameScene.sceneryWrapper, 
                             self.gameScene.actorsWrapper) #TODO can make local vars for scenery to tidy up        
    
    '''
    Halt any running events, unload any assets, etc
    ''' 
    def unloadScene(self):
        self.soundPlayer.stopSound()
        self.musicPlayer.stopSong()
        
    def addEvent(self,event):
        self.gameEvents.append(event)
    
    