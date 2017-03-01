'''
Created on Mar 1, 2017

@author: Robert
'''

#should create the init function for the game first (since need a sound effect player etc

import unittest, pygame

from actors import SimpleBox
from player_actions import ActionMove, ActionColorSwap
from player_character import PlayerCharacter
from sound import SoundEffectPlayer

class Test(unittest.TestCase):

    def setUp(self):
#         pygame.init()
#         soundPlayer = SoundEffectPlayer()
#         self.simpleBox = SimpleBox()
#         self.playerCharacter = PlayerCharacter(simpleBox)
#         self.playerCharacter.actionMove=ActionMove()
#         self.playerCharacter.actionColorSwap = ActionColorSwap(['click'],soundPlayer)
        
    def testName(self):
        pass

    def tearDown(self):
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()