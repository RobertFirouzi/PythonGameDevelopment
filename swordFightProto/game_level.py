'''
Created on Mar 1, 2017

@author: Robert
'''

class GameLevel():
    def __init__(self, actors=[], scenery=[], events=[], layout = []):
        self.actors = actors
        self.scenery = scenery
        self.events = events
        self.layout = layout
        