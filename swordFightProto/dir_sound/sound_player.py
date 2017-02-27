'''
Created on Feb 25, 2017

@author: Robert
'''

import pygame

class MusicPlayer():
    def __init__(self, playlist=[]):
        self.playlist=playlist
        self.songIndex = 0
        
    def playRepeat(self, song=''):
        if song == '':
            pygame.mixer.music.load(self.playlist[self.songIndex])
            pygame.mixer.music.play(-1) #-1 means repeate
            
class SoundEffectPlayer():
    def __init__(self, soundDict={}):
        self.soundDict = soundDict
        
    def loadSound(self, path, sound, ext):
        if self.soundDict.get(sound) == None:
            newSound = pygame.mixer.Sound(path+sound+ext)
            self.soundDict[sound] = newSound

    def playSound(self, sound):
        self.soundDict[sound].play()