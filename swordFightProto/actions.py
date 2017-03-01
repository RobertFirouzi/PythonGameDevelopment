'''
Created on Feb 25, 2017

@author: Robert
'''

import parameters as PRAM

#Action can take optional params and a link to thje soundplayer if a se is associated
#If there are soundeffects associated, pass their names as params
class ActionBase():
    def __init__(self,params=[],soundPlayer= None):
        self.params=params
        self.soundPlayer = soundPlayer

    def act(self, character, params=[]):
        pass
    
class ActionMove(ActionBase):
    def __init__(self, params=[], soundPlayer= None):
        super(ActionMove, self).__init__(params, soundPlayer)
    
    def act(self,character,params=[]):
        if params[0]=='up':
            if character.actor.y>0:
                character.actor.y-=character.actor.moveSpeed
        elif params[0]=='down':
            if character.actor.y<PRAM.DISPLAY_HEIGHT:  # @UndefinedVariable
                character.actor.y+=character.actor.moveSpeed
        elif params[0]=='left':
            if character.actor.x>0:
                character.actor.x-=character.actor.moveSpeed
        elif params[0]=='right':
            if character.actor.x<PRAM.DISPLAY_WIDTH: # @UndefinedVariable
                character.actor.x+=character.actor.moveSpeed

#plays the param[0] sound effect.  Actions could play sound effects depending on outcome?        
class ActionColorSwap(ActionBase):
    def __init__(self, params, soundPlayer):   
        super(ActionColorSwap, self).__init__(params, soundPlayer)
    
    def act(self, character, params=[]):
        colorSwapMethod = getattr(character.actor, "colorSwap", None)
        if callable(colorSwapMethod):
            character.actor.colorSwap()
            self.soundPlayer.playSound(self.params[0])
        
        
        
        
        
        