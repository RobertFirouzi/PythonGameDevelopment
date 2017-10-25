### PARAMETERS ###

import pygame

DEBUG_MENU =\
'''
Select a Debug Option:
0) Quit
1) Change Character Speed
2) Edit Scenery
3) Edit Tilemap
>>>'''
QUIT = 0
CHAR_SPEED = 1
SCENERY = 2
TILEMAP = 3

MOVESPEED_MENU=\
'''
Enter an integer value for character Move Speed, (or -99 to cancel).
(0 is no movement, 10 is average, 30 is insane)
>>>'''

SCENERY_MENU=\
'''
Choose Scenery Type
0) Quit
1) Background
2) Foreground 
>>>'''
BACKGROUND = 1
FOREGROUND = 2

TILEMAP_MENU=\
'''
Choose Tilemap Type
0) Quit
1) Lower
2) Upper
3) Barrier
>>>'''
LOWER = 1
UPPER = 2
BARRIER = 3

SCENERY_EDIT_MENU =\
'''
What will you change?
0) Quit
1) filePath (load new image)
2) visible sections
3) scrolling
4) alpha (True or False)
5) layer
>>>
'''
FILEPATH = 1
VISIBILE_SECTIONS = 2
SCROLLING = 3
ALPHA = 4
LAYER = 5

#Class to run debug mode - allows user programmer to change in game variables to test different areas of code
class DebugLooper():
    def __init__(self, game):
        self.debug = False
        self.game = game #need a reference to main game to be able to tweak game variables

    def run(self):
        self.keepGoing = True
        try:
            while self.debug:
                devInput = input(DEBUG_MENU)
                print('You chose: ' + str(devInput))
                devInput = int(devInput)
                if devInput == QUIT:
                    self.debug=False
                elif devInput == CHAR_SPEED:
                    self.changePlayerSpeed()
                elif devInput == SCENERY:
                    self.changeScenery()
                elif devInput == TILEMAP:
                    self.changeTilemap()

        except Exception as e:
            print('debug loop failed with exception')
            print(e)

    def changeScenery(self):
        keepGoing = True

        while keepGoing:
            devInput = int(input(SCENERY_MENU))
            if devInput == BACKGROUND:
                self.editScenery(background = True)
            elif devInput == FOREGROUND:
                self.editScenery(background = False)
            elif devInput == QUIT:
                keepGoing = False
            else:
                print('That is not a menu option')

    def changeTilemap(self):
        keepGoing = True

        while keepGoing:
            devInput = int(input(TILEMAP_MENU))
            if devInput == LOWER:
                print('edit lower')
            elif devInput == UPPER:
                print('edit upper')
            elif devInput == BARRIER:
                print('edit barrier')
            elif devInput == QUIT:
                keepGoing = False
            else:
                print('That is not a menu option')

    def changePlayerSpeed(self):
        devInput = int(input(MOVESPEED_MENU))
        if devInput != -99:
            self.game.player.moveSpeed = devInput
            print('Players speed changed to: ' + str(devInput))

    def editScenery(self, background = True):
        if background:
            scenery = self.game.levelData.backgrounds
        else:
            scenery = self.game.levelData.foregrounds
        if len(scenery) == 0:
            print('No panoramas')
            return

        print('Which panorama will you edit?')
        i = 0
        for panorama in scenery:
            print(str(i+1) + ': ' + str(panorama.filePath))
            i+=1

        devInput = int(input('''or -99 to cancel
>>>'''))
        if devInput <0 or devInput > i:
            print('Quit')
            return

        index = devInput -1 #index into array of scenery objects to edit

        keepGoing = True
        while keepGoing: #TODO
            devInput = int(input(SCENERY_EDIT_MENU))
            if devInput == FILEPATH:
                scenery[index].filePath = 'C:\\Users\\Robert\\repositories\\gameDev\\swordFightProto\\dir_image\\background_blue.jpg'
                if scenery[index].alpha:
                    scenery[index].image = pygame.image.load(scenery[index].filePath).convert_alpha()
                else:
                    scenery[index].image = pygame.image.load(scenery[index].filePath).convert()
            elif devInput == VISIBILE_SECTIONS:
                print('edit visibility')
            elif devInput == SCROLLING:
                print('edit scrolling')
            elif devInput == ALPHA:
                print('edit alpha')
            elif devInput == LAYER:
                print('edit layer')
            elif devInput == QUIT:
                keepGoing = False

















