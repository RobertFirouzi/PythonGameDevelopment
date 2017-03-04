'''
Created on Feb 25, 2017

@author: Robert
'''

import parameters as PRAM
from event import EventSound

class ActionBase():
    def __init__(self,character,params=()):
        self.character=character
        self.params=params

    def act(self, character, params=()):
        return ''
    
class ActionMove(ActionBase):
    def __init__(self, character, params=()):
        super(ActionMove, self).__init__(character, params)
    
    def act(self,params=()):
        if params=='up':
            if self.character.actor.y>0:
                self.character.actor.y -= self.character.actor.moveSpeed
        elif params=='down':
            if self.character.actor.y<PRAM.DISPLAY_HEIGHT:  # @UndefinedVariable
                self.character.actor.y += self.character.actor.moveSpeed
        elif params=='left':
            if self.character.actor.x>0:
                self.character.actor.x -= self.character.actor.moveSpeed
        elif params=='right':
            if self.character.actor.x < PRAM.DISPLAY_WIDTH: # @UndefinedVariable
                self.character.actor.x += self.character.actor.moveSpeed
        return '' #TODO return a move event here to check the characters new position?
        

#plays the param[0] sound effect.  Actions could play sound effects depending on outcome?        
class ActionColorSwap(ActionBase):
    def __init__(self, character, params = ()):   
        super(ActionColorSwap, self).__init__(character, params)
    
    def act(self, params=()):
        retVal=''
        colorSwapMethod = getattr(self.character.actor, "colorSwap", None)
        if callable(colorSwapMethod):
            self.character.actor.colorSwap()
            retVal = EventSound(PRAM.SOUND_COLORSWAP)
        return retVal        
        
        
        
        
        