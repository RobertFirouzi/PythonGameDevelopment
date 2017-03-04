'''
Created on Mar 4, 2017

@author: Robert
'''

#actions can return a generated event to be queued and run following pygame events
class EventGeneratedBase():
    def __init__(self, params=()):
        self.params=params

    #define in extended class
    def run(self):
        pass

#plays a sound effect
class EventSound(EventGeneratedBase):
    def __init__(self, sound, params=()):
        super(EventSound, self).__init__(params)
        self.sound=sound

#plays a music track
class EventSong(EventGeneratedBase):
    def __init__(self, song, params=()):
        super(EventSong, self).__init__(params)
        self.song=song

#class to run all generated events.  Has reference to game object to have access to all engine components
class EventHandler():
    def __init__(self, game):
        self.game = game
    
    #run all the events in the queue
    def handleEvents(self):
        while len(self.game.gameEvents)>0:
            retVal = self.run(self.game.gameEvents.pop()) #once an event has run, it can be discarded
            if retVal != '':
                self.game.gameEvents.push(retVal) #events can generate additional events
        return
        
    def run(self, event):
        retVal = ''
        if type(event) is EventSound:
            self.game.soundPlayer.playSound(event.sound)
        elif type(event) is EventSong:
            self.game.musicPlayer.playSong(event.song)
        return retVal


