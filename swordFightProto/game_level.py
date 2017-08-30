'''
Created on Mar 1, 2017

@author: Robert
'''

'''
Data container class for a game level, contained within the game object
@param actors
@param scenery
@param levelEvents
@param gameEvents
@param layout
'''

import utility as UTIL
import parameters as PRAM

class LevelData():
    def __init__(self,
                 size = (10,10), 
                 tileMap = '', #filename of a jpg of all tiles
                 lowerTiles = [], #displayed below all actors
                 upperTiles = [], #displayed above all actors
                 borders = [], #4 bits, one to represent each direction
                 eventTiles = {}, #Events are indexed based on coordiante pairs                 
                 actors = [], #static or dynamic, displayed in order of Y coords
                 backgrounds = [], #list of background objects
                 foregrounds = [], #list of foreground objects
                 gameEvents = [] #added to event queue on level load
                 ):
        self.size = size
        self.tileMap = tileMap
        self.lowerTiles = lowerTiles
        self.upperTiles = upperTiles
        self.borders = borders
        self.eventTiles = eventTiles
        self.actors = actors
        self.backgrounds = backgrounds
        self.foregrounds = foregrounds
        self.gameEvents = gameEvents
        
        
        pass
    
class GameLevel():
    def __init__(self,
                 size = (10,10), 
                 actorsWrapper = None, 
                 sceneryWrapper = None, 
                 levelEvents = [], 
                 gameEvents = [], 
                 layoutWrapper = None,
                 gameCamera = None):
        self.size =size
        self.actorsWrapper = actorsWrapper
        self.sceneryWrapper = sceneryWrapper
        self.levelEvents = levelEvents
        self.gameEvents = gameEvents #automatically load and run when level loads
        self.layoutWrapper = layoutWrapper
        self.gameCamera = gameCamera
        
        self.renderQueue = []
        self.backgroundQueue = []

    
    '''
    Based on start and end position, and actor size, add a bounding box to the 
        renderQueue (in pixels) for a section of the gameLevel that needs to be
        rendered on the render changes call 
    '''
    def addRenderBox(self, size, origin, destination, direction):
        if direction == PRAM.UP:
            minx = origin[0]
            miny = destination[1]
            maxx = destination[0] + size[0]
            maxy = origin[1] + size[1]
        elif direction == PRAM.DOWN:
            minx = origin[0]
            miny = origin[1]
            maxx = destination[0] + size[0]
            maxy = destination[1] + size[1]
        elif direction == PRAM.LEFT:
            minx = destination[0] 
            miny = origin[1]
            maxx = origin[0] + size[0]
            maxy = destination[1] + size[1]
        else: #right
            minx = origin[0]
            miny = origin[1]
            maxx = destination[0] + size[0]
            maxy = destination[1] + size[1]
        
        mapSizeX = len(self.layoutWrapper.layout[0]) * PRAM.TILESIZE
        mapSizeY = len(self.layoutWrapper.layout) * PRAM.TILESIZE
        
        #get the entire tile
        minx = minx - (minx % PRAM.TILESIZE)
        miny = miny - (miny % PRAM.TILESIZE)
        maxx = (maxx//PRAM.TILESIZE + 1)*PRAM.TILESIZE
        maxy = (maxy//PRAM.TILESIZE + 1)*PRAM.TILESIZE        
             
        if minx<0:
            minx = 0
        if miny<0:
            miny = 0
        if maxx > mapSizeX:
            maxx = mapSizeX 
        if maxy > mapSizeY:
            maxy = mapSizeY            
                
        self.renderQueue.append((minx, maxx, miny, maxy))
    
    '''
        Based on an actor and target, add tiles to the render queue that should
            be redrawn
            TODO: might deprecate this in favor of returning a pixel box
    '''
    def calcRenderChanges(self, actor, origin, target, direction):
        actorTileAbsolute = UTIL.calcTileFromPix(origin)
        actorTileSize = UTIL.calcTileSizeFromPix(actor.size)
        actorPixRelative = UTIL.calcCharPix(origin, actor.size)
        actorTileRelative = UTIL.calcTileFromPix(actorPixRelative)

        mapSizeX = len(self.layoutWrapper.layout[0])
        mapSizeY = len(self.layoutWrapper.layout)
                
        if direction == PRAM.UP:
            minXTile = actorTileAbsolute[0] - 1
            maxXTile = actorTileAbsolute[0] + actorTileSize[0] + 1
            maxYTile = actorTileAbsolute[1] + actorTileSize[1] +1
            minYTile = actorTileAbsolute[1] - (target[1] - actorTileRelative[1])             
        
        elif direction == PRAM.DOWN:
            minXTile = actorTileAbsolute[0] - 1
            maxXTile = actorTileAbsolute[0] + actorTileSize[0] + 1
            minYTile = actorTileAbsolute[1]
            maxYTile = actorTileAbsolute[1] + (target[1] - actorTileRelative[1]) + actorTileSize[1] +1
               
        elif direction == PRAM.LEFT:
            maxXTile = actorTileAbsolute[0] + actorTileSize[0] + 1
            minXTile = actorTileAbsolute[0] - (actorTileRelative[0] - target[0]) - actorTileSize[0]            
            minYTile = actorTileAbsolute[1]
            maxYTile = actorTileAbsolute[1] + actorTileSize[1] +1        
                
        else: #right
            minXTile = actorTileAbsolute[0]
            maxXTile = actorTileAbsolute[0] + (target[0]- actorTileRelative[0]) + actorTileSize[0] +1              
            minYTile = actorTileAbsolute[1]
            maxYTile = actorTileAbsolute[1] + actorTileSize[1] +1               
        
        #add a - 2 fudge factor to accomodate scrolling BR
        minXTile -= 2
        minYTile -= 2
                
        if minXTile < 0:
            minXTile = 0
        if maxXTile > mapSizeX:
            maxXTile = mapSizeX        
        if minYTile < 0:
            minYTile = 0   
        if maxYTile > mapSizeY:
            maxYTile = mapSizeY
        
        for x in range(minXTile, maxXTile):
            for y in range(minYTile, maxYTile):
                self.backgroundQueue.append((self.layoutWrapper.layout[y][x],(x,y)))

        maxXTile +=2
        maxYTile +=2
        minXTile -= 2
        minYTile -= 2
        
        if minXTile < 0:
            minXTile = 0
        if maxXTile > mapSizeX:
            maxXTile = mapSizeX        
        if minYTile < 0:
            minYTile = 0   
        if maxYTile > mapSizeY:
            maxYTile = mapSizeY
        
        for x in range(minXTile, maxXTile):
            for y in range(minYTile, maxYTile):
                self.renderQueue.append((self.layoutWrapper.layout[y][x],(x,y)))
                                                    
    def addActor(self, actor):
        self.actorsWrapper.actors.append(actor)
                
'''
Data container for a game menu, which can be loaded as an event (akin to loading a level).
    EG load the title screen, or options, save/load etc...
'''
class GameMenu():
    def __init__(self, 
                 actorsWrapper = None, 
                 sceneryWrapper = None, 
                 levelEvents = [], 
                 gameEvents = [], 
                 layoutWrapper = []):
        self.actorsWrapper = actorsWrapper
        self.sceneryWrapper = sceneryWrapper
        self.levelEvents = levelEvents
        self.gameEvents = gameEvents
        self.layoutWrapper = layoutWrapper

'''
Loads a cutscene
'''
class GameCutscene(): #TODO
    def __init__(self, cutscene = []):
        self.cutscene = cutscene
        
    
class LayoutWrapper():
    def __init__(self, tileDict = {}, layout = [], size = [10,10]):
        self.tileDict = tileDict
        self.layout = layout
        self.size = size

'''
Defines the event that is triggered on a level tile, and how it is triggered
    Defines number of times that event can be triggered (or -1 for infinite)
'''
class LevelEvent():
    def __init__(self, trigger, gameEvent, triggers = -1):
        self.trigger = trigger
        self.gameEvent = gameEvent
        self.triggers = triggers

'''
Defines the look and behavior of a single level tile.  Lower is the graphic that
    sits on top of a background image but below all other layers.  Mid sits on top of
    the lower but is still behind actors (decorations, switches, etc).  Upper is above 
    all actors.
    Barrier defines if the tile is not traversable in any direction
    levelEvent defines an event that is triggered on this tile.  Can be set to trigger
    on touch or on action or 
'''
class LevelTile():
    def __init__(self, 
                 lower = '', 
                 mid = '', 
                 upper = '', 
                 barrier = 0b0000, 
                 levelEvent = None,
#                  background = False,
                 foreground = False,
                 changed = False):
        self.lower = lower
        self.mid = mid
        self.upper = upper
        self.barrier = barrier
        self.levelEvent = levelEvent
#         self.background = background
        self.foreground = foreground 
        self.changed = changed

'''
Level events require a trigger event (whereas gameEvents run immediately)
    This event triggers if it is touched. Default subject is player.
    size and position can be hardcoded, or set as the size and position of 
    another actor (if the event should move with an actor)
    level tiles can also trigger an event if touched
'''
class LevelTriggerTouch():
    def __init__(self, gameEvent, size = (0,0) , position = (0,0), subject = 'player'):
        self.gameEvent = gameEvent
        self.size = size
        self.position = position
        self.subject = subject

    def notify(self):
        if self.subject.actor.position[0] >= self.position[0] and self.subject.actor.position[0] <= self.position[0] + self.size[0]:
            if self.subject.actor.position[1] >= self.position[1] and self.subject.actor.position[1] <= self.position[1] + self.size[1]:
                return self.gameEvent
        return None




    
    