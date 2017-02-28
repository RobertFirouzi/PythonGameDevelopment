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
sys.path.append(PROJECTPATH+'dir_sound')

from sound_object import SoundWrapper  # @UnresolvedImport
from log_errors import logError  # @UnresolvedImport

class MusicPlayer():
    def __init__(self, musicDict={}):
        self.musicDict = musicDict
        errorSong = SoundWrapper('song', __file__.replace('sound_player.py','dir_music\\'), 'ERROR', '.mp3' )
        self.loadSong(errorSong)
        
    def loadSong(self, soundWrapper):
        retVal = True
        if soundWrapper.soundType =='song':
            if self.musicDict.get(soundWrapper.sound) == None:
                if(os.path.exists(str(soundWrapper.fullPath))):   
                    self.musicDict[soundWrapper.sound] = soundWrapper
                else:
                    logError('MusicPlayer','loadSong', 
                             'path [' +soundWrapper.fullPath+ '] not found')
                    retVal = False
            else:
                logError('MusicPlayer','loadSong', 
                         'tried to reload [' +soundWrapper.fullPath+ '], but this already exists')
                retVal = False
        else:
            retVal = False
            logError('MusicPlayer','loadSong', 'load song with type: ' + str(soundWrapper.soundType))
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
            pygame.mixer.music.load(self.musicDict.get(song).fullPath)
            pygame.mixer.music.play(-1)
        return retVal

# note that a sound object must be created first, then can be played            
class SoundEffectPlayer():
    def __init__(self, soundDict={}):
        self.soundDict = soundDict
        errorSound = SoundWrapper('sound', __file__.replace('sound_player.py','dir_soundeffects\\'), 'ERROR', '.wav' )
        self.loadSound(errorSound)
        
    def loadSound(self, soundWrapper):
        retVal = True    
        if soundWrapper.soundType =='sound':
            if self.soundDict.get(soundWrapper.sound) == None:
                if(os.path.exists(str(soundWrapper.fullPath))):   
                    soundWrapper.soundObject = pygame.mixer.Sound(soundWrapper.fullPath) #save the sound file in the object
                    self.soundDict[soundWrapper.sound] = soundWrapper
                else:
                    logError('SoundEffectPlayer','loadSound', 'path [' +soundWrapper.fullPath+ '] not found')
                    retVal = False                
            else:
                logError('SoundEffectPlayer','loadSound', 'tried to reload [' +soundWrapper.fullPath+ '], but this already exists')
                retVal = False
        else:
            retVal=False
            logError('SoundEffectPlayer','loadSound', 'load sound with type: ' + str(soundWrapper.soundType))                                 
        return retVal

    def playSound(self, sound):
        retVal = True
        if self.soundDict.get(sound) == None:
            logError('SoundEffectPlayer','playSound', 'sound [' +sound+ '] not found in dict')
            retVal = False
            if sound != 'ERROR': #prevent infinite recursion
                self.playSound('ERROR')
        else:
            self.soundDict[sound].soundObject.play()
        return retVal
   
#set volume value [0,1.0] of sound in dictionary    
    def setSoundVolume(self,sound,volume):
        retVal = True
        if volume>1.0 or volume<0:
            logError('SoundEffectPlayer','setSoundVolume', 'val '+str(volume)+' out of range')            
            retVal = False
        elif self.soundDict.get(sound) == None:  
            logError('SoundEffectPlayer','playSound', 'sound [' +sound+ '] not found in dict')
            retVal = False
        else: 
            self.soundDict.get(sound).soundObject.set_volume(volume)
        return retVal
        
        
        
        
