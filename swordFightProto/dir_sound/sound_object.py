'''
Created on Feb 28, 2017

@author: Robert
'''

#object which holds information for a sound effect, ambient track or music track
class SoundWrapper():
    def __init__(self, soundType, path, sound, ext):
        self.soundType=soundType
        self.path=path
        self.sound=sound
        self.ext=ext
        self.fullPath = path+sound+ext