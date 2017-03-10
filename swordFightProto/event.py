'''
Created on Mar 4, 2017

@author: Robert
'''

import parameters as PRAM
import utility as UTIL
'''
Base class is extended for specific event types
'''
class EventGeneratedBase():
    def __init__(self, params=()):
        self.params=params

    #define in extended class
    def run(self):
        pass

'''
An event for when a character attempts to move
'''

class EventMove(EventGeneratedBase):
    def __init__(self, character, direction, params = ()):
        super(EventMove, self).__init__(params)
        self.character = character
        self.direction = direction

'''
If a character moves, notify any listeners, passing in the character and the 
    listener list
'''
class EventNotifyMove(EventGeneratedBase):
    def __init__(self, character, params = ()):
        super(EventNotifyMove, self).__init__(params)
        self.character = character

'''
Play a sound effect with the sound player
@param sound
'''
class EventSound(EventGeneratedBase):
    def __init__(self, sound, params = ()):
        super(EventSound, self).__init__(params)
        self.sound = sound

'''
Plays a music track
@param song
'''
class EventSong(EventGeneratedBase):
    def __init__(self, song, params = ()):
        super(EventSong, self).__init__(params)
        self.song=song

class EventSetInput(EventGeneratedBase):
    def __init__(self, inputType, params = ()):
        super(EventSetInput, self).__init__(params)
        self.inputType = inputType

'''
Loads a new level into game
@param levelFile
'''
class EventLoadLevel(EventGeneratedBase):
    def __init__(self, levelFile, startingPosition = [0,0], params = ()):
        super(EventLoadLevel, self).__init__(params)
        self.levelFile = levelFile
        self.startingPosition = startingPosition

class EventLoadMenu(EventGeneratedBase):
    def __init__(self, menuFile, params = ()):
        super(EventLoadMenu, self).__init__(params)
        self.menuFile = menuFile
        
#TODO
class EventLoadCutscene(EventGeneratedBase):
    def __init__(self, cutsceneFile, params = ()):
        super(EventLoadCutscene, self).__init__(params)
        self.cutsceneFile = cutsceneFile

'''
Runs all defined events.  Needs a reference to the game object to access engine objectd
@param game
'''
class EventHandler():
    def __init__(self, game):
        self.game = game
    
    '''
    Runs all the events in the game event queue.  Events can return new events
        which are pushed on to the stack and immediately run (be careful of infinite loops!)
    '''
    def handleEvents(self):
        while len(self.game.gameEvents) > 0:
            event = self.game.gameEvents.pop()
            if event != '':
                self.run(event)
        return
     
    '''
    Runs an event, and returns a new event if one is generated.  Access game engine
        objects to perform the events
    @param event
    @return event
    '''    
    def run(self, event):
        if type(event) is EventMove:
            char = event.character
            charPixel = char.getPosition()
            charSize = char.getSize()
            charPixel = [charPixel[0] + charSize[0]//2, charPixel[1] + charSize[1]*2//3] #adjust to middle of char
            charTile = UTIL.calcTileFromPix(charPixel) #relative tile that char appears to stand on
            layout = self.game.gameScene.layout
            
            if event.direction =='up':
                target = UTIL.calcTileFromPix([charPixel[0],charPixel[1]-char.moveSpeed])
                if target == charTile:
                    char.adjustPosition(0,-char.moveSpeed)
                else:
                    if layout[target[1]][target[0]].barrier & 0b0001: #barrier in the way
                        char.adjustPosition(0, (target[1]+1) * PRAM.TILESIZE - charPixel[1]) #move next to barrier
                    else:
                        char.adjustPosition(0,-char.moveSpeed)
                
            elif event.direction =='down':
                target = UTIL.calcTileFromPix([charPixel[0], charPixel[1] + char.moveSpeed])
                if target == charTile:
                    char.adjustPosition(0, char.moveSpeed)
                else:
                    if layout[target[1]][target[0]].barrier & 0b1000: #barrier in the way
                        char.adjustPosition(0, target[1] * PRAM.TILESIZE - charPixel[1]-1) #move next to barrier
                    else:
                        char.adjustPosition(0, char.moveSpeed)
                    
            elif event.direction =='left':
                target = UTIL.calcTileFromPix([charPixel[0] - char.moveSpeed, charPixel[1]])
                if target == charTile:
                    char.adjustPosition(-char.moveSpeed, 0) 
                else:
                    if layout[target[1]][target[0]].barrier & 0b0010: #barrier in the way
                        char.adjustPosition((target[0]+1) * PRAM.TILESIZE - charPixel[0], 0) #move next to barrier
                    else:
                        char.adjustPosition(-char.moveSpeed, 0)
                                                                              
            else: # 'right'
                target = UTIL.calcTileFromPix([charPixel[0] + char.moveSpeed, charPixel[1]])
                if target == charTile:
                    char.adjustPosition(char.moveSpeed, 0) 
                else:
                    if layout[target[1]][target[0]].barrier & 0b0100: #barrier in the way
                        char.adjustPosition(target[0] * PRAM.TILESIZE - charPixel[0]-1, 0) #move next to barrier
                    else:
                        char.adjustPosition(char.moveSpeed, 0)
            
            if target !=charTile:
                pass
                #TODO check for and add any events trigger by touching this tile

            if len(char.moveListeners) > 0:
                self.game.addEvent(EventNotifyMove(event.character))

        elif type(event) is EventNotifyMove:
            for listener in event.character.moveListeners:
                listenerEvent = listener.notify()
                if listenerEvent != None:
                    self.game.addEvent(listenerEvent)
        
        elif type(event) is EventSound:
            self.game.soundPlayer.playSound(event.sound)
        
        elif type(event) is EventSong:
            self.game.musicPlayer.playSong(event.song)
        
        elif type(event) is EventLoadLevel:
            self.game.loadLevel(event)
        
        elif type(event) is EventLoadMenu:
            self.game.loadMenu(event.menuFile)
        
        elif type(event) is EventLoadCutscene:
            self.game.loadCutscene(event.cutsceneFile)
        
        elif type(event) is EventSetInput:
            self.game.inputHandler.setInputBehavior(event.inputType)    
        
        return


