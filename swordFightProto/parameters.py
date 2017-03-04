'''
Created on Feb 24, 2017

@author: Robert
'''
import os

### PATHS ###
MUSIC_PATH = os.path.realpath('')+'\\dir_sound\\dir_music\\'
AMBIENCE_PATH = os.path.realpath('')+'\\dir_sound\\dir_ambience\\'
SOUND_PATH = os.path.realpath('')+'\\dir_sound\\dir_soundeffects\\'
IMAGE_PATH = os.path.realpath('')+'\\dir_image\\'
LEVEL_PATH = os.path.realpath('')+'\\dir_levels\\'

### SCREEN ###
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

### ACTORS ###
SIMPLE_BOX_WIDTH = 60
SIMPLE_BOX_HEIGHT = 60

### COLORS ###
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 128, 255)
COLOR_ORANGE = (255, 100, 0)

### IMAGES ###
IMAGE_LIBRARY = ['ball.png'] #may not be needed

### IMAGE MAP ###
IMG_BALL = 'ball.png'
IMG_TEST = 'testsprite.png'

### SOUNDTRACK ###
MUSIC_PLAYLIST = [
    'ERROR',
    'saga7-Wind',
    'saga7-Water']

AMBIENCE = ['city']

SOUNDEFFECTS = [
    'ERROR',
    'click']

### SONGMAP ###
SONG_SAGAWATER = 'saga7-Water'
SONG_TEST = 'testsong'
SONG_ERROR = 'ERROR'

### AMBIANTMAP ###
AMB_CITY = 'city'

### SOUNDMAP ###
SOUND_COLORSWAP = 'click'
SOUND_ERROR = 'ERROR'
SOUND_TEST = 'testeffect'

### GAME LEVELS ###
LEVEL_LIBRARY = ['level_test01'] #may not be needed

### LEVEL MAP ###
LEV_TEST1 = 'level_test01'


