'''
Created on Mar 1, 2017

@author: Robert
'''
from sound import MusicPlayer, SoundEffectPlayer, SoundWrapper
from player_character import PlayerCharacter
from actions import ActionColorSwap, ActionMove
import parameters as PRAM

'''
Generates the sound and music players, and loads the entire soundtrack into
    the dictionaries of each
'''
def soundPlayerFactory():
    musicPlayer = MusicPlayer()
    soundPlayer = SoundEffectPlayer()
    for song in PRAM.MUSIC_PLAYLIST:
        musicPlayer.loadSong(SoundWrapper('song', PRAM.MUSIC_PATH, song, '.mp3'))
    for sound in PRAM.SOUNDEFFECTS:
        soundPlayer.loadSound(SoundWrapper('sound', PRAM.SOUND_PATH, sound, '.wav'))
    for ambience in PRAM.AMBIANCE:
        soundPlayer.loadSound(SoundWrapper('sound', PRAM.AMBIANCE_PATH, ambience, '.wav'))        
    return musicPlayer, soundPlayer

'''
Initialize the player character and create the starting actions.  May not start
with an actor initialized
@param actor
'''
def playerFactory(actor=None):
    player = PlayerCharacter(actor)
    actionMove = ActionMove(player)
    defaultAction = ActionColorSwap(player)
    player.actionMove=actionMove.act
    player.defaultAction=defaultAction.act
    return player

    
    
    
