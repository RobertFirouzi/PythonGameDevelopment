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
                 levelEvent = None):
        self.lower = lower
        self.mid = mid
        self.upper = upper
        self.barrier = barrier
        self.levelEvent = levelEvent


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




    
    