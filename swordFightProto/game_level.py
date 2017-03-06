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
    def __init__(self, actors = [], scenery = [], levelEvents = [], gameEvents = [], layout = []):
        self.actors = actors
        self.scenery = scenery
        self.levelEvents = levelEvents
        self.gameEvents = gameEvents
        self.layout = layout
        
'''
Data container for a game menu, which can be loaded as an event (akin to loading a level).
    EG load the title screen, or options, save/load etc...
'''
class GameMenu():
    def __init__(self, actors = [], scenery = [], levelEvents = [], gameEvents = [], layout = []):
        self.actors = actors
        self.scenery = scenery
        self.levelEvents = levelEvents
        self.gameEvents = gameEvents
        self.layout = layout

'''
Loads a cutscene
'''
class GameCutscene():
    def __init__(self, cutscene = []):
        self.cutscene = cutscene