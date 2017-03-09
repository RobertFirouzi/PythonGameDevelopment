'''
Created on Feb 25, 2017

@author: Robert
'''

import parameters as PRAM
from event import EventSound, EventMove

'''
Base class for an Action object.  Extend for specific functionality
    Contains a link to the character which contains the action
@param character
'''
class ActionBase():
    def __init__(self,character,params=()):
        self.character=character
        self.params=params

    def act(self, character, params=()):
        return ''

'''
Moves the character's actor based on its movement speed
@Param character
@return None 
'''    
class ActionMove(ActionBase):
    def __init__(self, character, params=()):
        super(ActionMove, self).__init__(character, params)
    
    def act(self, direction):
        return EventMove(self.character, direction)
#         retVal = ''
#         if params=='up':
#             if self.character.actor.position[1]>0:
#                 self.character.actor.position[1] -= self.character.moveSpeed
#                 retVal = EventMoved(self.character)
#         elif params=='down':
#             if self.character.actor.position[1]<PRAM.DISPLAY_HEIGHT:  # @UndefinedVariable
#                 self.character.actor.position[1] += self.character.moveSpeed
#                 retVal = EventMoved(self.character)
#         elif params=='left':
#             if self.character.actor.position[0]>0:
#                 self.character.actor.position[0] -= self.character.moveSpeed
#                 retVal = EventMoved(self.character)
#         elif params=='right':
#             if self.character.actor.position[0] < PRAM.DISPLAY_WIDTH: # @UndefinedVariable
#                 self.character.actor.position[0] += self.character.moveSpeed
#                 retVal = EventMoved(self.character)
#         return retVal

        

'''
Performs colorSwap on the character's actor containing the action, if they own this method
    returns a sound effect action
@Param character
@return EventSound 
'''      
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
        
        
        
        
        