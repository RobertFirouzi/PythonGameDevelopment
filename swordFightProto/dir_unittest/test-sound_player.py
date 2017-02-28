'''
Created on Feb 26, 2017

@author: Robert
'''
import unittest
import os,sys

sys.path.append(os.path.realpath('')+'\\..\\dir_sound\\')
from sound_player import *
from sound_object import *
import pygame

class TestSoundPlayers(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.musicPlayer = MusicPlayer()
        self.soundEffectPlayer = SoundEffectPlayer()
        soundPath = os.path.realpath('')+'\\..\\dir_sound\\'
        self.musicPath = soundPath+'dir_music\\'
        self.effectPath = soundPath+'dir_soundeffects\\'
        
### MusicPlayer() ###
    def test_loadSong(self):
        self.assertEqual(self.musicPlayer.loadSong(SoundWrapper('song', self.musicPath, 'testsong', '.mp3')), True)
        self.assertEqual(self.musicPlayer.loadSong(SoundWrapper('notsong', self.musicPath, 'testsong', '.mp3')), False)
        self.assertEqual(self.musicPlayer.loadSong(SoundWrapper('song', self.musicPath, 'songnotfound', '.mp3')), False)
        self.assertEqual(self.musicPlayer.loadSong(SoundWrapper('song', self.musicPath, 'testsong', '.mp3')), False) #already loaded
        
    def test_playSong(self):
        self.assertEqual(self.musicPlayer.playSong('testsong'), True)
        self.assertEqual(self.musicPlayer.playSong('songnotfound'), False)
        self.assertEqual(self.musicPlayer.playSong('testsong',1), True) #play song once              

### SoundEffectPlayer() ###
    def test_loadSound(self):
        self.assertEqual(self.soundEffectPlayer.loadSound(SoundWrapper('sound', self.effectPath, 'testeffect', '.wav')), True)
        self.assertEqual(self.soundEffectPlayer.loadSound(SoundWrapper('sound', self.effectPath, 'effectnotfound', '.wav')), False)
        self.assertEqual(self.soundEffectPlayer.loadSound(SoundWrapper('sound', self.effectPath, 'testeffect', '.wav')), False) #already loaded

    def test_playSound(self):
        self.assertEqual(self.soundEffectPlayer.playSound('testeffect'), True)
        self.assertEqual(self.soundEffectPlayer.playSound('effectnotfound'), False)            
  
    def test_setSoundVolume(self):
        self.assertEqual(self.soundEffectPlayer.setSoundVolume('testeffect',0), True)
        self.assertEqual(self.soundEffectPlayer.setSoundVolume('testeffect',0.62), True)  
        self.assertEqual(self.soundEffectPlayer.setSoundVolume('testeffect',1.0), True)                           
        self.assertEqual(self.soundEffectPlayer.setSoundVolume('testeffect',1.001), False) 
        self.assertEqual(self.soundEffectPlayer.setSoundVolume('testeffect',-1.0), False)       
        self.assertEqual(self.soundEffectPlayer.setSoundVolume('effectnotfound',5), False) 
        self.assertEqual(self.soundEffectPlayer.setSoundVolume('effectnotfound',0.5), False) 
          
    def tearDown(self):
        pass
#         self.musicPlayer.dispose()
#         self.soundEffectPlayer.dispose()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()