'''
Created on Feb 24, 2017

@author: Robert
'''

import parameters as PRAM

'''
Class contains the dictionary which has the reference to all loaded sprites, and
    the list of scenery items to place.  Sprites are loaded only once to the dictionary
    but can be placed as many times as they appear in the list
'''
class ActorsWrapper():
    def __init__(self, actorDict = {}, actors = []):
        self.actorDict = actorDict
        self.actors = actors

'''
Draws a box
@param color
@param width, height, startx, starty
'''
class SimpleBox():
    def __init__(self, color = PRAM.COLOR_BLUE, width = PRAM.SIMPLE_BOX_WIDTH, # @UndefinedVariable
                 height = PRAM.SIMPLE_BOX_HEIGHT, x = 100, y = 100): # @UndefinedVariable
        self.color=color
        self.width=width
        self.height=height
        self.x=x
        self.y=y   
        self.moveSpeed = 10
    
    '''
    Swaps its color between 2 predefined values
    '''
    def colorSwap(self):
        if self.color == PRAM.COLOR_BLUE: # @UndefinedVariable
            self.setColor(PRAM.COLOR_ORANGE) # @UndefinedVariable
        else:
            self.setColor(PRAM.COLOR_BLUE) # @UndefinedVariable
        
    def setColor(self,color):
        self.color=color