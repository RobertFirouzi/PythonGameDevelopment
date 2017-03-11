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

class ActorBase():
    def __init__(self, size, position, direction = 'right'):
        self.size = size
        self.position = position
        self.direction = direction
    
    def setPosition(self, position = [0,0]):
        self.position = position
    
    def getPosition(self):
        return self.position

'''
Draws a box
@param color
@param width, height, startx, starty
'''
class SimpleBox(ActorBase):
    def __init__(self, color = PRAM.COLOR_BLUE, size = [PRAM.SIMPLE_BOX_WIDTH, # @UndefinedVariable
                 PRAM.SIMPLE_BOX_HEIGHT], position =[100,100]): # @UndefinedVariable
        super(SimpleBox, self).__init__(size, position)
        self.color=color

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