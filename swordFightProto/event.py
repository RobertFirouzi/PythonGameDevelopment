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
    def __init__(self, eventType = '', params=()):
        self.eventType = eventType 
        self.params=params

'''
An event for when a character attempts to move
'''

class EventMove(EventGeneratedBase):
    def __init__(self, character, direction, eventType = 'MOVE', params = ()):
        super(EventMove, self).__init__(eventType, params)
        self.character = character
        self.direction = direction

class EventDefaultAction(EventGeneratedBase):
    def __init__(self, character, eventType = 'DEFAULTACTION', params = ()):
        super(EventDefaultAction, self).__init__(eventType, params)
        self.character = character
'''
If a character moves, notify any listeners, passing in the character and the 
    listener list
'''
class EventNotifyMove(EventGeneratedBase):
    def __init__(self, character, eventType = 'NOTIFYMOVE', params = ()):
        super(EventNotifyMove, self).__init__(eventType, params)
        self.character = character

'''
Play a sound effect with the sound player
@param sound
'''
class EventSound(EventGeneratedBase):
    def __init__(self, sound, eventType = 'SOUND', params = ()):
        super(EventSound, self).__init__(eventType, params)
        self.sound = sound

'''
Plays a music track
@param song
'''
class EventSong(EventGeneratedBase):
    def __init__(self, song, eventType = 'SONG', params = ()):
        super(EventSong, self).__init__(eventType, params)
        self.song=song

class EventSetInput(EventGeneratedBase):
    def __init__(self, inputType, eventType = 'SETINPUT', params = ()):
        super(EventSetInput, self).__init__(eventType, params)
        self.inputType = inputType

'''
Loads a new level into game
@param levelFile
'''
class EventLoadLevel(EventGeneratedBase):
    def __init__(self, levelFile, startingPosition = [0,0], eventType = 'LOADLEVEL', params = ()):
        super(EventLoadLevel, self).__init__(eventType, params)
        self.levelFile = levelFile
        self.startingPosition = startingPosition

class EventLoadMenu(EventGeneratedBase):
    def __init__(self, menuFile, eventType = 'LOADMENU', params = ()):
        super(EventLoadMenu, self).__init__(eventType, params)
        self.menuFile = menuFile
        
#TODO
class EventLoadCutscene(EventGeneratedBase):
    def __init__(self, cutsceneFile, eventType = 'LOADCUTSCENE', params = ()):
        super(EventLoadCutscene, self).__init__(eventType, params)
        self.cutsceneFile = cutsceneFile



'''
Runs all defined events.  Needs a reference to the game object to access engine objectd
@param game
'''
class EventHandler():
    def __init__(self, game, eventDict = {}):
        self.game = game
        self.eventDict = eventDict
        
    '''
    Runs all the events in the game event queue.  Events can return new events
        which are pushed on to the stack and immediately run (be careful of infinite loops!)
    '''
    def handleEvents(self):
        while len(self.game.gameEvents) > 0:
            event = self.game.gameEvents.pop()
            if event != '':
                self.eventDict[event.eventType](event)
        return
    
    def runMove(self, event):
        char = event.character
        charPixRelative = UTIL.calcCharPix(char.actor)
        charTileRelative = UTIL.calcTileFromPix(charPixRelative) #relative tile that char appears to stand on
        
        #for re-rendering calculations
        charTileSize = UTIL.calcTileSizeFromPix(char.getSize()) 
        charTileAbsolute = UTIL.calcTileFromPix(char.getPosition()) #tile the actor is in  
        layout = self.game.gameScene.layoutWrapper.layout
        mapSizeX = len(layout[0])
        mapSizeY = len(layout)
                      
        if event.direction =='up':
            char.setDirection('up')
            targetTile = UTIL.calcTileFromPix([charPixRelative[0],charPixRelative[1]-char.moveSpeed])
            if targetTile == charTileRelative:
                char.adjustPosition(0,-char.moveSpeed)
            else:
                if layout[targetTile[1]][targetTile[0]].barrier & 0b0001: #barrier in the way
                    char.adjustPosition(0, (targetTile[1]+1) * PRAM.TILESIZE - charPixRelative[1]) #move next to barrier
                else:
                    char.adjustPosition(0,-char.moveSpeed)            

            #Check for tiles which have a potential graphics change            
            minXTile = charTileAbsolute[0] - 1
            maxXTile = charTileAbsolute[0] + charTileSize[0] + 1
            if minXTile < 0:
                minXTile = 0
            if maxXTile > mapSizeX:
                maxXTile = mapSizeX
            maxYTile = charTileAbsolute[1] + charTileSize[1] +1
            minYTile = charTileAbsolute[1] - (targetTile[1] - charTileRelative[1])         
            if maxYTile > mapSizeY:
                maxYTile = mapSizeY
            if minYTile < 0:
                minYTile = 0
                
            for x in range(minXTile, maxXTile):
                for y in range(minYTile, maxYTile):
                    layout[y][x].changed = True
            
        elif event.direction =='down':
            char.setDirection('down')
            targetTile = UTIL.calcTileFromPix([charPixRelative[0], charPixRelative[1] + char.moveSpeed])
            if targetTile == charTileRelative:
                char.adjustPosition(0, char.moveSpeed)
            else:
                if layout[targetTile[1]][targetTile[0]].barrier & 0b1000: #barrier in the way
                    char.adjustPosition(0, targetTile[1] * PRAM.TILESIZE - charPixRelative[1]-1) #move next to barrier
                else:
                    char.adjustPosition(0, char.moveSpeed)
            
            #Check for tiles which have a potential graphics change            
            minXTile = charTileAbsolute[0] - 1
            maxXTile = charTileAbsolute[0] + charTileSize[0] + 1
            if minXTile < 0:
                minXTile = 0
            if maxXTile > mapSizeX:
                maxXTile = mapSizeX
            minYTile = charTileAbsolute[1]
            maxYTile = charTileAbsolute[1] + (targetTile[1] - charTileRelative[1]) + charTileSize[1] +1
            if maxYTile > mapSizeY:
                maxYTile = mapSizeY            
            for x in range(minXTile, maxXTile):
                for y in range(minYTile, maxYTile):
                    layout[y][x].changed = True
                
        elif event.direction =='left':
            char.setDirection('left')
            targetTile = UTIL.calcTileFromPix([charPixRelative[0] - char.moveSpeed, charPixRelative[1]])
            if targetTile == charTileRelative:
                char.adjustPosition(-char.moveSpeed, 0) 
            else:
                if layout[targetTile[1]][targetTile[0]].barrier & 0b0010: #barrier in the way
                    char.adjustPosition((targetTile[0]+1) * PRAM.TILESIZE - charPixRelative[0], 0) #move next to barrier
                else:
                    char.adjustPosition(-char.moveSpeed, 0)

            #Check for tiles which have a potential graphics change            
            maxXTile = charTileAbsolute[0] + charTileSize[0] + 1
            minXTile = charTileAbsolute[0] - (charTileRelative[0] - targetTile[0]) - charTileSize[0]
            if minXTile < 0:
                minXTile = 0
            if maxXTile > mapSizeX:
                maxXTile = mapSizeX                
            minYTile = charTileAbsolute[1]
            maxYTile = charTileAbsolute[1] + charTileSize[1] +1        
            if maxYTile > mapSizeY:
                maxYTile = mapSizeY
            for x in range(minXTile, maxXTile):
                for y in range(minYTile, maxYTile):
                    layout[y][x].changed = True
                                                                          
        else: # 'right'
            char.setDirection('right')
            targetTile = UTIL.calcTileFromPix([charPixRelative[0] + char.moveSpeed, charPixRelative[1]])
            if targetTile == charTileRelative:
                char.adjustPosition(char.moveSpeed, 0) 
            else:
                if layout[targetTile[1]][targetTile[0]].barrier & 0b0100: #barrier in the way
                    char.adjustPosition(targetTile[0] * PRAM.TILESIZE - charPixRelative[0]-1, 0) #move next to barrier
                else:
                    char.adjustPosition(char.moveSpeed, 0)

            #Check for tiles which have a potential graphics change            
            minXTile = charTileAbsolute[0]
            maxXTile = charTileAbsolute[0] + (targetTile[0]- charTileRelative[0]) + charTileSize[0] +1
            if maxXTile > mapSizeX:
                maxXTile = mapSizeX                
            minYTile = charTileAbsolute[1]
            maxYTile = charTileAbsolute[1] + charTileSize[1] +1        
            if maxYTile > mapSizeY:
                maxYTile = mapSizeY
            for x in range(minXTile, maxXTile):
                for y in range(minYTile, maxYTile):
                    layout[y][x].changed = True
        
        char.actor.changed = True #re-render the character
                            
        #check if the camera needs to be adjusted
        if char.actor.isFocus:
            self.game.gameCamera.panToChar(char.getPosition())
        
        #Check if the targetTile tile has an event that triggers on touch
        if targetTile !=charTileRelative:
            targetTileTile = layout[targetTile[1]][targetTile[0]]
            if targetTileTile.levelEvent != None:
                if targetTileTile.levelEvent.trigger == PRAM.TRIG_TOUCH:
                    self.game.addEvent(targetTileTile.levelEvent.gameEvent)

        if len(char.moveListeners) > 0:
            self.game.addEvent(EventNotifyMove(event.character))
            

    def runDefaultAction(self, event):
        triggered = False
        char = event.character
        charPixRelative = UTIL.calcCharPix(char.actor)
        charTileRelative = UTIL.calcTileFromPix(charPixRelative) #relative tile that char appears to stand on
        layout = self.game.gameScene.layoutWrapper.layout           
        
        if layout[charTileRelative[1]][charTileRelative[0]].levelEvent != None: #check the space you are standing on
            if layout[charTileRelative[1]][charTileRelative[0]].levelEvent.trigger == PRAM.TRIG_ACTION:
                self.game.addEvent(layout[charTileRelative[1]][charTileRelative[0]].levelEvent.gameEvent)
                triggered = True
        #now check the tile next to you that you are facing
        elif char.actor.direction =='up': 
            targetTile = UTIL.calcTileFromPix([charPixRelative[0],charPixRelative[1]-PRAM.TILESIZE])
            if layout[targetTile[1]][targetTile[0]].levelEvent != None: 
                if layout[targetTile[1]][targetTile[0]].levelEvent.trigger == PRAM.TRIG_ACTION:
                    self.game.addEvent(layout[targetTile[1]][targetTile[0]].levelEvent.gameEvent)
                    triggered = True
                
        elif char.actor.direction =='down':
            targetTile = UTIL.calcTileFromPix([charPixRelative[0], charPixRelative[1] + PRAM.TILESIZE])
            if layout[targetTile[1]][targetTile[0]].levelEvent != None:                 
                if layout[targetTile[1]][targetTile[0]].levelEvent.trigger == PRAM.TRIG_ACTION:
                    self.game.addEvent(layout[targetTile[1]][targetTile[0]].levelEvent.gameEvent)
                    triggered = True    
                
        elif char.actor.direction =='left':
            targetTile = UTIL.calcTileFromPix([charPixRelative[0] - PRAM.TILESIZE, charPixRelative[1]])
            if layout[targetTile[1]][targetTile[0]].levelEvent != None:                     
                if layout[targetTile[1]][targetTile[0]].levelEvent.trigger == PRAM.TRIG_ACTION:
                    self.game.addEvent(layout[targetTile[1]][targetTile[0]].levelEvent.gameEvent)
                    triggered = True
                                                                          
        else: # 'right'
            targetTile = UTIL.calcTileFromPix([charPixRelative[0] + PRAM.TILESIZE, charPixRelative[1]])
            if layout[targetTile[1]][targetTile[0]].levelEvent != None: 
                if layout[targetTile[1]][targetTile[0]].levelEvent.trigger == PRAM.TRIG_ACTION:
                    self.game.addEvent(layout[targetTile[1]][targetTile[0]].levelEvent.gameEvent)
                    triggered = True           
            
        if not triggered: #no level event, so perform characters default action
            self.game.addEvent(char.defaultAction())           
    
    def runNotifyMove(self, event):
        for listener in event.character.moveListeners:
            listenerEvent = listener.notify()
            if listenerEvent != None:
                self.game.addEvent(listenerEvent)
    
    def runSound(self, event):
        self.game.soundPlayer.playSound(event.sound)   
    
    def runSong(self, event):
        self.game.musicPlayer.playSong(event.song)
    
    def runSetInput(self, event):
        self.game.inputHandler.setInputBehavior(event.inputType)    
    
    def runLoadLevel(self, event):
        self.game.loadLevel(event)          

    def runLoadMenu(self, event):
        self.game.loadMenu(event.menuFile)
    
    def runLoadCutscene(self, event):
        self.game.loadCutscene(event.cutsceneFile)

