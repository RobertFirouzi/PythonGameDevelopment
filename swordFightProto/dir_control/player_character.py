'''
Created on Feb 25, 2017

@author: Robert
'''

import sys,os
sys.path.append(os.path.realpath('')+'\\dir_control')
sys.path.append(os.path.realpath('')+'\\dir_params')

from def_size import * # @UnresolvedImport
from player_actions import ActionMove, ActionDefault # @UnresolvedImport

class PlayerCharacter():
    def __init__(self, actor):
        self.actor = actor #link to the actor player is controlling
        self.defaultAction = self.colorSwap
    
    def performAction(self,action):
        if type(action) is ActionMove:
            self.move(action)
        if type(action) is ActionDefault:
            self.defaultAction(action)
        return
    
    #will need to pass in more information about location/scene to implement logic    
    def move(self,action):
        if action.direction=='up':
            if self.actor.y>0:
                self.actor.y-=self.actor.moveSpeed
        elif action.direction=='down':
            if self.actor.y<DISPLAY_HEIGHT:  # @UndefinedVariable
                self.actor.y+=self.actor.moveSpeed
        elif action.direction=='left':
            if self.actor.x>0:
                self.actor.x-=self.actor.moveSpeed
        elif action.direction=='right':
            if self.actor.x<DISPLAY_WIDTH: # @UndefinedVariable
                self.actor.x+=self.actor.moveSpeed
        
        return
     
    def colorSwap(self,action):
        self.actor.colorSwap()    