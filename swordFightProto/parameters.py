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


### SCREEN ###
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

### INPUT TYPES###
INPTYPE_OBSERVER = 'observe'
INPTYPE_MENU = 'menu'
INPTYPE_NORMAL = 'normal'

### KEYS ### - pygame.<keyname>
INPUT_ACTION = 32 #pygame space bar
INPUT_STATUS = 13 #pygame enter key
INPUT_UP = 273
INPUT_DOWN = 274
INPUT_LEFT = 276
INPUT_RIGHT = 275

### ACTORS ###
SIMPLE_BOX_WIDTH = 60
SIMPLE_BOX_HEIGHT = 60

### LISTENER TYPES ###
LISTENER_MOVE = 'move'

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






