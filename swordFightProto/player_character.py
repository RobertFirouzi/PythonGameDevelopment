'''
Created on Feb 25, 2017

@author: Robert
'''

'''
Class to contain data and actions for a PC.  Actions are added to the object
    and modified dynamically
@param actor
'''
class PlayerCharacter():
    def __init__(self, actor=None):
        self.actor = actor #link to the actor player is controlling
