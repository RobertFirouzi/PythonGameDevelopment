'''
Created on Mar 4, 2017

@author: Robert
'''

import parameters as PRAM
import sys, importlib
from game_level import GameLevel, GameCutscene, GameMenu, LevelTriggerTouch, LayoutWrapper
from event import EventLoadMenu
from scenery import StaticSprite, SceneryWrapper
from actors import ActorsWrapper
import pygame
from parameters import TILESIZE

'''
The highest level object which contains references to the game level and
    all of the game engine objects
@param player
@param musicPlayer
@param soundPlayer
@param renderer
'''
class Game():
    def __init__(self, player = None, 
                 musicPlayer = None, 
                 soundPlayer = None, 
                 renderer = None,
                 gameCamera = None):
        self.player = player
        self.musicPlayer = musicPlayer
        self.soundPlayer = soundPlayer
        self.renderer = renderer
        self.gameCamera = gameCamera
        
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
        gameLevel object.  Loads the game events from the level to be immediately run
    @param levelFile
    '''
    def loadLevel(self, eventLoadLevel):
        self.unloadScene() 
        sys.path.append(PRAM.LEVEL_PATH)
        level = importlib.import_module(eventLoadLevel.levelFile)                       
        sys.path.pop()
        
        self.gameScene = GameLevel(
            level.size,
            self.loadActors(level.actors), #returns an actorsWrapper object
            self.loadImages(level.scenery, level.background, level.foreground), #returns a sceneryWrapper object
            level.levelEvents,
            level.gameEvents,
            self.loadLayout(level.tileDict, level.layout, level.size), #returns a layoutWrapper object
            self.gameCamera) 
        
        layoutHack = self.gameScene.layoutWrapper.layout
        for x in range(0,150):
            for y in range(0,150):
                if layoutHack[y][x].mid == 'trunk':
                    layoutHack[y][x].mid = ''
                    layoutHack[y][x].lower = 'trunk'
        
        for x in range(0,150):
            for y in range(0,15):
                if layoutHack[y][x].lower != 'trunk':
                    layoutHack[y][x].lower = ''
#                 layoutHack[y][x].mid = ''
#                 layoutHack[y][x].upper = ''            
#                 layoutHack[y][x].background = True
                layoutHack[y][x].foreground = True

        for x in range(0,150):
            for y in range(15,25):
                layoutHack[y][x].foreground = True
                        
        for y in range(0,150):
            for x in range(0,15):
                if layoutHack[y][x].lower != 'trunk':
                    layoutHack[y][x].lower = ''
#                 layoutHack[y][x].mid = ''
#                 layoutHack[y][x].upper = ''            
#                 layoutHack[y][x].background = True                
                layoutHack[y][x].foreground = True
                
        for y in range(0,150):
            for x in range(135,150):
                if layoutHack[y][x].lower != 'trunk':
                    layoutHack[y][x].lower = ''
#                 layoutHack[y][x].mid = ''
#                 layoutHack[y][x].upper = ''            
#                 layoutHack[y][x].background = True  
                layoutHack[y][x].foreground = True
                
        for x in range(0,150):
            for y in range(135,150):
#                 layoutHack[y][x].lower = ''
#                 layoutHack[y][x].mid = ''
#                 layoutHack[y][x].upper = ''            
                layoutHack[y][x].foreground = True

        for x in range(0,150):
            for y in range(125,135):
                layoutHack[y][x].foreground = True
                                                    
        for event in self.gameScene.gameEvents: #add to eventQueue, e.g. song to play
            self.addEvent(event)
        
        #currently triggered on the tile
#         for event in self.gameScene.levelEvents: #the triggers need to be initialized for level events
#             if type(event) is LevelTriggerTouch:
#                 if event.subject == 'player':
#                     self.player.addListener(PRAM.LISTENER_MOVE, event)
#                     event.subject = self.player

        self.gameScene.addActor(self.player.actor) #add the player character to the level actors list
        self.player.setPosition(eventLoadLevel.startingPosition)
        self.gameCamera.maxPosition = [  #TODO - may need to modify this to create a bounding box
            (level.size[0] - PRAM.DISPLAY_TILE_WIDTH)*PRAM.TILESIZE,
            (level.size[1] - PRAM.DISPLAY_TILE_HEIGHT)*PRAM.TILESIZE]


    def loadMenu(self, menuFile):
        self.unloadScene()
        sys.path.append(PRAM.MENU_PATH)
        menu = importlib.import_module(menuFile)
        sys.path.pop()
        
        self.gameScene = GameMenu(
            self.loadActors(menu.actors), #returns an actorWrapper object
            [],#self.loadImages(menu.scenery, False), #returns a sceneryWrapper object
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
            if type(actor) is StaticSprite: #TODO this will be type Sprite or similar
                if actorDict.get(actor.image) == None:
                    actorDict[actor.image] = pygame.image.load(actor.path+actor.image).convert_alpha()
                    
        return ActorsWrapper(actorDict, actors)

    
    #Creates a dictionary with the reference being an image name, and the item being a
    #   loaded image file.  Each unique image only needs to be loaded once
    
    def loadImages(self, scenery, background, foreground):
        imageDict = {}
        for sprite in scenery:
            if type(sprite) is StaticSprite:
                if imageDict.get(sprite.image) == None:
                    imageDict[sprite.image] = pygame.image.load(sprite.path+sprite.image).convert()

        for pic in background:
            if pic.alpha == True:
                imageDict[pic.image] = pygame.image.load(pic.path+pic.image).convert_alpha()
            else:
                imageDict[pic.image] = pygame.image.load(pic.path+pic.image).convert()

        for pic in foreground:
            if pic.alpha == True:
                imageDict[pic.image] = pygame.image.load(pic.path+pic.image).convert_alpha()
            else:
                imageDict[pic.image] = pygame.image.load(pic.path+pic.image).convert()
                        
        return SceneryWrapper(imageDict, scenery, background, foreground)

    def loadLayout(self, tileDict, layout, size):
        layoutDict = {}
        for x in range(size[0]):
            for y in range(size[1]):
                tile = layout[x][y]
                if tile.lower != '' and layoutDict.get(tile.lower) == None:
                    layoutDict[tile.lower] = pygame.image.load(tileDict[tile.lower]).convert()
                if tile.mid != '' and layoutDict.get(tile.mid) == None:
                    layoutDict[tile.mid] = pygame.image.load(tileDict[tile.mid]).convert()
                if tile.upper != '' and layoutDict.get(tile.upper) == None:
                    layoutDict[tile.upper] = pygame.image.load(tileDict[tile.upper]).convert()
                                                            
        return LayoutWrapper(layoutDict, layout, size)
       
    def render(self):
        self.renderer.render(self.gameScene)  
    
    
    # Halt any running events, unload any assets, etc
     
    def unloadScene(self):
        #TODO - empty game event queue
        self.soundPlayer.stopSound()
        self.musicPlayer.stopSong()
        
    def addEvent(self,event):
        self.gameEvents.append(event)
    
    