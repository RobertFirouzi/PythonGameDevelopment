'''
Created on Feb 24, 2017

@author: Robert
'''
import pygame
import parameters as PRAM
from setup import soundPlayerFactory,playerCharacterFactory,renderFactory,gameLevelFactory

def initializeLevel(renderActors,renderScenery,playerCharacter,level=[],params=[]):
    gameLevel = gameLevelFactory(level, params)
    renderActors.actors = gameLevel.actors
    renderScenery.scenery = gameLevel.scenery
    playerCharacter.actor = gameLevel.actors[0]
    return gameLevel

### SETUP ###
pygame.init()  # @UndefinedVariable
screen = pygame.display.set_mode((PRAM.DISPLAY_WIDTH, PRAM.DISPLAY_HEIGHT))
CLOCK = pygame.time.Clock() 
DONE = False

### GAME ENGINE ###
gameLevel = gameLevelFactory()
musicPlayer, soundPlayer = soundPlayerFactory()
renderActors, renderScenery = renderFactory(screen, gameLevel.actors, gameLevel.scenery)
#TODO - get soundPlayer out of here, then easy to move all into initializeLevel function
playerCharacter = playerCharacterFactory(gameLevel.actors[0], soundPlayer)

#think where this should be called?  (music/ambiance track should be within gameLevel)
musicPlayer.playSong('saga7-Water')
soundPlayer.playSound('city')
soundPlayer.setSoundVolume('city',0.4)

while not DONE:
        ### CHECK THE EVENT QUEUE ###
        for event in pygame.event.get():         
            if event.type == pygame.QUIT:  # @UndefinedVariable
                DONE = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # @UndefinedVariable 
                playerCharacter.defaultAction(playerCharacter)
                    
        ### CHECK BUTTON PRESSES ###   
        pressed = pygame.key.get_pressed()    
        #DIRECTIONAL               
        if pressed[pygame.K_UP]:  # @UndefinedVariable
            playerCharacter.actionMove(playerCharacter,['up'])
        if pressed[pygame.K_DOWN]:  # @UndefinedVariable
            playerCharacter.actionMove(playerCharacter,['down'])
        if pressed[pygame.K_LEFT]:  # @UndefinedVariable
            playerCharacter.actionMove(playerCharacter,['left'])
        if pressed[pygame.K_RIGHT]:  # @UndefinedVariable
            playerCharacter.actionMove(playerCharacter,['right'])
        
        ### DRAW THE GRAPHICS ###
        renderScenery.render()
        renderActors.render()
        pygame.display.flip()
        CLOCK.tick(60)

#this will only run if the module is run as the main module, not if imported
if __name__ == '__main__':
    pass #nop

