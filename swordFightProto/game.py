'''
Created on Mar 4, 2017

@author: Robert
'''

#Highest level class which contains reference to all game objects
class Game():
    def __init__(self, 
                 player = None,
                 gameLevel = None, 
                 musicPlayer = None, 
                 soundPlayer = None, 
                 renderer = None,
                 gameEvents = None,
                 eventHandler = None):
        self.player = player
        self.gameLevel = gameLevel
        self.musicPlayer = musicPlayer
        self.soundPlayer = soundPlayer
        self.renderer = renderer
        self.gameEvents=gameEvents
        self.eventHandler = eventHandler
    
    #define the method to init a game level here
    def initializeLevel(self, level):
        pass