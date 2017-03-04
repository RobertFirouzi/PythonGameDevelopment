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

#class to run all generated events
class EventHandler():
    def __init__(self, game):
        self.game = game
    
    #run all the events in the queue
    def handleEvents(self):
        while len(self.game.events)>0:
            self.run(self.game.events.pop())
        return
        
    def run(self, event):
        pass


