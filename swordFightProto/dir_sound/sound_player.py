'''
Created on Feb 25, 2017

@author: Robert
'''

#Modules not unit tested:
#(none)

import pygame
import sys,os
PROJECTPATH = __file__.replace('dir_sound\sound_player.py',"")
sys.path.append(PROJECTPATH+'dir_logging')

from log_errors import logError  # @UnresolvedImport

class MusicPlayer():
    def __init__(self, musicDict={}):
        self.musicDict=musicDict
        self.loadSong(os.path.realpath('')+'\\dir_sound\\dir_music\\', 'ERROR', '.mp3')
        
    def loadSong(self, path, song, ext):
        retVal = True
        if self.musicDict.get(song) == None:
            if(os.path.exists(str(path+song+ext))):   
                newSong = str(path+song+ext)
                self.musicDict[song] = newSong
            else:
                logError('MusicPlayer','loadSong', 'path [' +path+song+ext+ '] not found')
                retVal = False
        else:
            logError('MusicPlayer','loadSong', 'tried to reload [' +path+song+ext+ '], but this already exists')
            retVal = False
        return retVal
                
    #playthroughs is how many times to play the song, but -1 means repeat    
    def playSong(self, song, playthroughs=-1):
        retVal = True
        if self.musicDict.get(song) == None:
            logError('MusicPlayer','playSong', 'song [' + song+ '] not found in dict')
            retVal = False
            if song != 'ERROR': #avoid infinite recursion
                self.playSong('ERROR',1)
        else:
            pygame.mixer.music.load(self.musicDict.get(song))
            pygame.mixer.music.play(-1)
        return retVal

# note that a sound object must be created first, then can be played            
class SoundEffectPlayer():
    def __init__(self, soundDict={}):
        self.soundDict = soundDict
        self.loadSound(os.path.realpath('')+'\\dir_sound\\dir_soundeffects\\', 'ERROR', '.wav')
        
    def loadSound(self, path, sound, ext):
        retVal = True
        if self.soundDict.get(sound) == None:
            if(os.path.exists(str(path+sound+ext))):   
                newSound = pygame.mixer.Sound(path+sound+ext)
                self.soundDict[sound] = newSound
            else:
                logError('SoundEffectPlayer','loadSound', 'path [' +path+sound+ext+ '] not found')
                retVal = False                
        else:
            logError('SoundEffectPlayer','loadSound', 'tried to reload [' +path+sound+ext+ '], but this already exists')
            retVal = False
        return retVal

    def playSound(self, sound):
        retVal = True
        if self.soundDict.get(sound) == None:
            logError('SoundEffectPlayer','playSound', 'sound [' +sound+ '] not found in dict')
            retVal = False
            if sound != 'ERROR': #prevent infinite recursion
                self.playSound('ERROR')
        else:
            self.soundDict[sound].play()
        return retVal
   
#set volume value [0,1.0] of sound in dictionary    
    def setSoundVolume(self,sound,volume):
        retVal = True
        if volume>1.0 or volume<0:
            logError('SoundEffectPlayer','setSoundVolume', 'val '+str(volume)+' out of range')            
            retVal = False
        elif self.soundDict.get(sound) == None:  
            retVal = False
        else: 
            self.soundDict.get(sound).set_volume(volume)
        return retVal
        
        
        
        
