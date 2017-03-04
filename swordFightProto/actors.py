'''
Created on Feb 24, 2017

@author: Robert
'''

import parameters as PRAM

'''
Draws a box
@param color
@param width, height, startx, starty
'''
class SimpleBox():
    def __init__(self, color = PRAM.COLOR_BLUE, width = PRAM.SIMPLE_BOX_WIDTH, # @UndefinedVariable
                 height = PRAM.SIMPLE_BOX_HEIGHT, x = 0, y = 0): # @UndefinedVariable
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