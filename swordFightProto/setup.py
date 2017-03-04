'''
Created on Mar 1, 2017

@author: Robert
'''
from sound import MusicPlayer, SoundEffectPlayer, SoundWrapper
from player_character import PlayerCharacter
from actions import ActionColorSwap, ActionMove
from game_level import GameLevel
from scenery import SolidBackground, StaticSprite
from actors import SimpleBox
from game import Game

import os, pygame
import parameters as PRAM

MUSIC_PATH = os.path.realpath('')+'\\dir_sound\\dir_music\\'
AMBIENCE_PATH = os.path.realpath('')+'\\dir_sound\\dir_ambience\\'
SOUND_PATH = os.path.realpath('')+'\\dir_sound\\dir_soundeffects\\'
IMAGE_PATH = os.path.realpath('')+'\\dir_image\\'

#TODO define these in a separate module
MUSIC_PLAYLIST = [
    'saga7-Wind',
    'saga7-Water']
SOUNDEFFECTS = ['click']
AMBIENCE = ['city']

#creates, loads and returns the music and sound effect players for pygame
def soundPlayerFactory():
    musicPlayer = MusicPlayer()
    soundPlayer = SoundEffectPlayer()
    for song in MUSIC_PLAYLIST:
        musicPlayer.loadSong(SoundWrapper('song', MUSIC_PATH, song, '.mp3'))
    for sound in SOUNDEFFECTS:
        soundPlayer.loadSound(SoundWrapper('sound', SOUND_PATH, sound, '.wav'))
    for ambience in AMBIENCE:
        soundPlayer.loadSound(SoundWrapper('sound', AMBIENCE_PATH, ambience, '.wav'))        
    return musicPlayer, soundPlayer


def gameFactory(player = None,
                gameLevel = None, 
                musicPlayer = None, 
                soundPlayer = None, 
                renderer = None,
                events = None,
                eventHandler = None):
    game = Game(player, gameLevel, musicPlayer, soundPlayer, renderer, events, eventHandler)
    return game

def playerFactory(actor):
    player = PlayerCharacter(actor)
    actionMove = ActionMove(player)
    defaultAction = ActionColorSwap(player)
    player.actionMove=actionMove.act
    player.defaultAction=defaultAction.act
    return player
    
#TODO - create a module template that contains information for a level to load 
def gameLevelFactory(level=[], params=[]):
    background = SolidBackground(PRAM.COLOR_BLACK)
    img_ball = StaticSprite(pygame.image.load(IMAGE_PATH+'ball.png'), (20,20))
    box = SimpleBox()  
    actors = []
    scenery = []
    layout = []
    events=[]
    actors.append(box)
    scenery.append(background)
    scenery.append(img_ball)
    gameLevel = GameLevel(actors, scenery, events, layout)
    
    return gameLevel
    
    
    
    
