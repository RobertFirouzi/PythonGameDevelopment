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
    def __init__(self, actors=[], scenery=[], levelEvents=[], gameEvents=[], layout = []):
        self.actors = actors
        self.scenery = scenery
        self.levelEvents = levelEvents
        self.gameEvents = gameEvents
        self.layout = layout
        