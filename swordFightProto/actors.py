'''
Created on Feb 24, 2017

@author: Robert
'''

import parameters as PRAM


class SimpleBox():
    def __init__(self, color = PRAM.COLOR_BLUE, width = PRAM.SIMPLE_BOX_WIDTH, # @UndefinedVariable
                 height = PRAM.SIMPLE_BOX_HEIGHT, x = 0, y = 0): # @UndefinedVariable
        self.color=color
        self.width=width
        self.height=height
        self.x=x
        self.y=y   
        self.moveSpeed = 10
    
    def colorSwap(self):
        if self.color == PRAM.COLOR_BLUE: # @UndefinedVariable
            self.setColor(PRAM.COLOR_ORANGE) # @UndefinedVariable
        else:
            self.setColor(PRAM.COLOR_BLUE) # @UndefinedVariable
        
    def setColor(self,color):
        self.color=color 