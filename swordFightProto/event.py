'''
Created on Mar 4, 2017

@author: Robert
'''

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
    def __init__(self, levelFile, params = ()):
        super(EventLoadLevel, self).__init__(params)
        self.levelFile = levelFile

#TODO
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
            retVal = self.run(self.game.gameEvents.pop()) #once an event has run, it can be discarded
            if retVal != '':
                self.game.gameEvents.push(retVal) #events can generate additional events
        return
     
    '''
    Runs an event, and returns a new event if one is generated.  Access game engine
        objects to perform the events
    @param event
    @return event
    '''    
    def run(self, event):
        retVal = ''
        if type(event) is EventSound:
            self.game.soundPlayer.playSound(event.sound)
        elif type(event) is EventSong:
            self.game.musicPlayer.playSong(event.song)
        elif type(event) is EventLoadLevel:
            self.game.loadLevel(event.levelFile)
        elif type(event) is EventLoadMenu:
            self.game.loadMenu(event.menuFile)
        elif type(event) is EventLoadCutscene:
            self.game.loadCutscene(event.cutsceneFile)
        elif type(event) is EventSetInput:
            self.game.inputHandler.setInputBehavior(event.inputType)    
        return retVal


