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
                self.eventDict[event.eventType](event )
        return
    
    def runMove(self, event):
        char = event.character
        charPixel = UTIL.calcCharPix(char.actor)
        charTile = UTIL.calcTileFromPix(charPixel) #relative tile that char appears to stand on
        charTileSize = UTIL.calcTileSizeFromPix(char.getSize())
        
        layout = self.game.gameScene.layoutWrapper.layout
        
        print('charpixel: ' + str(charPixel))
        print('charTile: ' + str(charTile))
        print('charTileSize: ' + str(charTileSize))                

        
        if event.direction =='up':
            char.setDirection('up')
            target = UTIL.calcTileFromPix([charPixel[0],charPixel[1]-char.moveSpeed])
            if target == charTile:
                char.adjustPosition(0,-char.moveSpeed)
            else:
                if layout[target[1]][target[0]].barrier & 0b0001: #barrier in the way
                    char.adjustPosition(0, (target[1]+1) * PRAM.TILESIZE - charPixel[1]) #move next to barrier
                else:
                    char.adjustPosition(0,-char.moveSpeed)
            
            #Check for tiles which have a potential graphics change
            maxX = charTile[0] + charTileSize[0]
            maxY = charTile[1] + charTileSize[1] +1
                        
            if maxY > len(layout): #stay in the index bounds
                maxY = len(layout)
            if maxX >= len(layout[0]):
                maxX = len(layout[0])
                
            for x in range (charTile[0], maxX):
                for y in range(target[1], maxY):
                    print('(' + str(x)+','+str(y)+')')
                    layout[y][x].changed = True
            
            print('minY: ' + str(maxY))
            print('maxX: ' + str(maxX))
            
        elif event.direction =='down':
            char.setDirection('down')
            target = UTIL.calcTileFromPix([charPixel[0], charPixel[1] + char.moveSpeed])
            if target == charTile:
                char.adjustPosition(0, char.moveSpeed)
            else:
                if layout[target[1]][target[0]].barrier & 0b1000: #barrier in the way
                    char.adjustPosition(0, target[1] * PRAM.TILESIZE - charPixel[1]-1) #move next to barrier
                else:
                    char.adjustPosition(0, char.moveSpeed)
            
            #Check for tiles which have a potential graphics change
            maxX = charTile[0] + charTileSize[0]
            minY = charTile[1] - charTileSize[1]
            maxY = target[1] + charTileSize[1]
                        
            if maxY > len(layout): #stay in the index bounds
                maxY = len(layout)
            if maxX >= len(layout[0]):
                maxX = len(layout[0])
            if minY < 0:
                minY = 0
                            
            for x in range (charTile[0], maxX):
                for y in range(minY, maxY):
                    print('(' + str(x)+','+str(y)+')')
                    layout[y][x].changed = True
            
            print('maxY: ' + str(maxY))
            print('maxX: ' + str(maxX))
            
                
        elif event.direction =='left':
            char.setDirection('left')
            target = UTIL.calcTileFromPix([charPixel[0] - char.moveSpeed, charPixel[1]])
            if target == charTile:
                char.adjustPosition(-char.moveSpeed, 0) 
            else:
                if layout[target[1]][target[0]].barrier & 0b0010: #barrier in the way
                    char.adjustPosition((target[0]+1) * PRAM.TILESIZE - charPixel[0], 0) #move next to barrier
                else:
                    char.adjustPosition(-char.moveSpeed, 0)
                                                                          
        else: # 'right'
            char.setDirection('right')
            target = UTIL.calcTileFromPix([charPixel[0] + char.moveSpeed, charPixel[1]])
            if target == charTile:
                char.adjustPosition(char.moveSpeed, 0) 
            else:
                if layout[target[1]][target[0]].barrier & 0b0100: #barrier in the way
                    char.adjustPosition(target[0] * PRAM.TILESIZE - charPixel[0]-1, 0) #move next to barrier
                else:
                    char.adjustPosition(char.moveSpeed, 0)
        
        #check if the camera needs to be adjusted
        if char.actor.isFocus:
            self.game.gameCamera.panToChar(char.getPosition())
        
        #Check if the target tile has an event that triggers on touch
        if target !=charTile:
            targetTile = layout[target[1]][target[0]]
            if targetTile.levelEvent != None:
                if targetTile.levelEvent.trigger == PRAM.TRIG_TOUCH:
                    self.game.addEvent(targetTile.levelEvent.gameEvent)

        if len(char.moveListeners) > 0:
            self.game.addEvent(EventNotifyMove(event.character))
            

    def runDefaultAction(self, event):
        triggered = False
        char = event.character
        charPixel = UTIL.calcCharPix(char.actor)
        charTile = UTIL.calcTileFromPix(charPixel) #relative tile that char appears to stand on
        layout = self.game.gameScene.layoutWrapper.layout           
        
        if layout[charTile[1]][charTile[0]].levelEvent != None: #check the space you are standing on
            if layout[charTile[1]][charTile[0]].levelEvent.trigger == PRAM.TRIG_ACTION:
                self.game.addEvent(layout[charTile[1]][charTile[0]].levelEvent.gameEvent)
                triggered = True
        #now check the tile next to you that you are facing
        elif char.actor.direction =='up': 
            target = UTIL.calcTileFromPix([charPixel[0],charPixel[1]-PRAM.TILESIZE])
            if layout[target[1]][target[0]].levelEvent != None: 
                if layout[target[1]][target[0]].levelEvent.trigger == PRAM.TRIG_ACTION:
                    self.game.addEvent(layout[target[1]][target[0]].levelEvent.gameEvent)
                    triggered = True
                
        elif char.actor.direction =='down':
            target = UTIL.calcTileFromPix([charPixel[0], charPixel[1] + PRAM.TILESIZE])
            if layout[target[1]][target[0]].levelEvent != None:                 
                if layout[target[1]][target[0]].levelEvent.trigger == PRAM.TRIG_ACTION:
                    self.game.addEvent(layout[target[1]][target[0]].levelEvent.gameEvent)
                    triggered = True    
                
        elif char.actor.direction =='left':
            target = UTIL.calcTileFromPix([charPixel[0] - PRAM.TILESIZE, charPixel[1]])
            if layout[target[1]][target[0]].levelEvent != None:                     
                if layout[target[1]][target[0]].levelEvent.trigger == PRAM.TRIG_ACTION:
                    self.game.addEvent(layout[target[1]][target[0]].levelEvent.gameEvent)
                    triggered = True
                                                                          
        else: # 'right'
            target = UTIL.calcTileFromPix([charPixel[0] + PRAM.TILESIZE, charPixel[1]])
            if layout[target[1]][target[0]].levelEvent != None: 
                if layout[target[1]][target[0]].levelEvent.trigger == PRAM.TRIG_ACTION:
                    self.game.addEvent(layout[target[1]][target[0]].levelEvent.gameEvent)
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

