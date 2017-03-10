'''
Created on Feb 24, 2017

@author: Robert
'''
import os

### PATHS ###
MUSIC_PATH = os.path.realpath('')+'\\dir_sound\\dir_music\\'
AMBIANCE_PATH = os.path.realpath('')+'\\dir_sound\\dir_ambiance\\'
SOUND_PATH = os.path.realpath('')+'\\dir_sound\\dir_soundeffects\\'
IMAGE_PATH = os.path.realpath('')+'\\dir_image\\'
LEVEL_PATH = os.path.realpath('')+'\\dir_levels\\'
MENU_PATH = os.path.realpath('')+'\\dir_menu\\'
CUTSCENE_PATH = os.path.realpath('')+'\\dir_cutscene\\'

'''
a 1600x896 screen gives about 50x32 tiles of size 32
33x19 of size 48 tiles
This makes a ~100x100 tile map reasonable, and provides a good 5 screens 
of scrolling

'''

### SCREEN ###
DISPLAY_WIDTH = 800 #1600 
DISPLAY_HEIGHT = 600 #900 
TILESIZE = 48

### INPUT TYPES###
INPTYPE_OBSERVER = 'observe'
INPTYPE_MENU = 'menu'
INPTYPE_NORMAL = 'normal'

### TRIGGER TYPES ###
TRIG_TOUCH = 'touch'
TRIG_ACTION = 'action'


### KEYS ### - pygame.<keyname>
INPUT_ACTION = 32 #pygame space bar
INPUT_STATUS = 13 #pygame enter key
INPUT_UP = 273
INPUT_DOWN = 274
INPUT_LEFT = 276
INPUT_RIGHT = 275

### ACTORS ###
SIMPLE_BOX_WIDTH = 50
SIMPLE_BOX_HEIGHT = 102

### LISTENER TYPES ###
LISTENER_MOVE = 'move'

### COLORS ###
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 128, 255)
COLOR_ORANGE = (255, 100, 0)
COLOR_WHITE = (255, 255, 255)

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

AMBIANCE = ['city']

SOUNDEFFECTS = [
    'ERROR',
    'click']

### SONGMAP ###
SONG_SAGAWATER = 'saga7-Water'
SONG_SAGAWIND = 'saga7-Wind'
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

### GAME MENUS ###
MENU_LIBRARY = ['menu_test01']

### MENU MAP ###
MENU_TEST1 = 'menu_test01'






