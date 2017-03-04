'''
Created on Mar 1, 2017

@author: Robert
'''

class GameLevel():
    def __init__(self, actors=[], scenery=[], levelEvents=[], layout = []):
        self.actors = actors
        self.scenery = scenery
        self.levelEvents = levelEvents
        self.layout = layout
        