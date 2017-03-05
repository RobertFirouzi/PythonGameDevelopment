'''
Created on Mar 5, 2017

@author: Robert
'''

'''
Class to store the type of input received (keydown, presseed, mousemove, etc) and
    the input trigger (arrow key, letter, mouse click...)
'''

#TODO create a mapping class/parameter
import parameters as PRAM

'''
Class defines which keys are mapped to which actions (allows for changing buttons during
    game play dynamically i.e. controller config)
@param up
@param down
@param left
@param right
@param default
'''
class ButtonMap():
    def __init__(self, 
                 up = PRAM.INPUT_UP, 
                 down = PRAM.INPUT_DOWN, 
                 left =  PRAM.INPUT_LEFT, 
                 right = PRAM.INPUT_RIGHT, 
                 default = PRAM.INPUT_DEFAULT):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.default = default                

'''
Class has the behaviors of each input dynamically assigned and processes input
each frame
@param game
@param player
@param buttonMap
'''
class InputHandler():
    def __init__(self, game = None, player = None, buttonMap = None):
        self.game = game
        self.player = player
        self.buttonMap = buttonMap
 
        #These behaviors are durnamically assigned based on game state       
        self.inputUpBehavior = self.movementUp
        self.inputDownBehavior = self.movementDown
        self.inputLeftBehavior = self.movementLeft
        self.inputRightBehavior = self.movementRight
        
        #IE the 'A' button, which may change behaviour dynamically based on sourounding
        self.inputActionBehavior = self.defaultAction 
      
    def handleInputs(self):
        while len(self.game.keydownEvents) > 0:
            event = self.game.keydownEvents.pop() 
            if event.key == self.buttonMap.default:
                self.inputActionBehavior()
            #TODO - add more key events here
        
        #check which keys are currently pressed down        
        if self.game.keysPressed[self.buttonMap.up]:
            self.inputUpBehavior()
        if self.game.keysPressed[self.buttonMap.down]:
            self.inputDownBehavior()
        if self.game.keysPressed[self.buttonMap.left]:
            self.inputLeftBehavior()
        if self.game.keysPressed[self.buttonMap.right]:
            self.inputRightBehavior()
        
        return

#TODO - should dirrectional events return an event for the queue?    
    def movementUp(self):
        self.player.actionMove('up')
        
    def movementDown(self):
        self.player.actionMove('down')
    
    def movementLeft(self):
        self.player.actionMove('left')
    
    def movementRight(self):
        self.player.actionMove('right')
    
    def defaultAction(self):
        self.game.addEvent(self.player.defaultAction()) #'default behavior'
    