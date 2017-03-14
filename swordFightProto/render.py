'''
Created on Feb 25, 2017

@author: Robert
'''

from actors import SimpleBox
from scenery import StaticSprite, SolidBackground
import utility as UTIL
import pygame
from game_level import GameLevel
import parameters as PRAM

'''
Class which renders images to the screen
@param screen
'''
class Renderer():
    def __init__(self, screen):
        self.screen = screen
        
        #explicit delceration of class fields
        self.cameraTile= (0,0)
        self.cameraOffset = (0,0)
        self.cameraPosition = (0,0)
    
    '''
     1) render background.
     2) render lower tiles 
     3) render mid tiles
     4) render actors
     5) render upper tiles
    '''
    def render(self, gameScene): #TODO - remove need for the brnach on gamescene type
        if type(gameScene) is GameLevel:
            self.cameraTile = gameScene.gameCamera.getTile()
            self.cameraOffset = gameScene.gameCamera.getOffset()
            self.cameraPosition = gameScene.gameCamera.getPosition()
            moveFlag = gameScene.gameCamera.moveFlag
    
#         self.renderScenery(gameScene.sceneryWrapper)
        
        if type(gameScene) is GameLevel:
            self.renderTiles(gameScene.layoutWrapper, moveFlag)
        self.renderActors(gameScene.actorsWrapper)
        if type(gameScene) is GameLevel:
            self.renderTiles(gameScene.layoutWrapper, moveFlag, False, False, True)
        
        if type(gameScene) is GameLevel:
            gameScene.gameCamera.moveFlag=False
    
    def renderTiles(self, layoutWrapper, moveFlag, lower = True, mid = True, upper = False):
        for y in range(PRAM.DISPLAY_TILE_HEIGHT):
            for x in range(PRAM.DISPLAY_TILE_WIDTH):
                tile = layoutWrapper.layout[y+self.cameraTile[1]][x+self.cameraTile[0]]
                if moveFlag == True or tile.changed == True:
                    location = UTIL.calcPixFromTile((x,y), -self.cameraOffset[0], -self.cameraOffset[1])
                    if lower:
                        if tile.lower != '':
                            self.screen.blit(layoutWrapper.tileDict[tile.lower], location)
                    if mid:
                        if tile.mid != '':
                            self.screen.blit(layoutWrapper.tileDict[tile.mid], location)
                    if upper:
                        if tile.upper != '':                    
                            self.screen.blit(layoutWrapper.tileDict[tile.upper], location)
                        tile.changed = False
                
        
            
    '''
    Render all scenery
    @param sceneryWrapper
    '''
    def renderScenery(self, sceneryWrapper):
        for feature in sceneryWrapper.scenery:
            if type(feature) is SolidBackground:
                self.screen.fill(feature.color)
                
            elif type(feature) is StaticSprite:
                self.screen.blit(sceneryWrapper.imageDict[feature.image], feature.location)
                
            elif type(feature) is SimpleBox:
                pygame.draw.rect(self.screen, feature.color, 
                                 pygame.Rect(feature.position[0], feature.position[1], 
                                             feature.size[0], feature.size[1]))                
        return
    
    '''
    Render all actors
    @param actors
    '''
    def renderActors(self, actorsWrapper):
        for actor in actorsWrapper.actors:
            if type(actor) is SimpleBox:
                pygame.draw.rect(self.screen, actor.color, 
                                 pygame.Rect(actor.position[0]+PRAM.BOX_FUDGE - self.cameraPosition[0], 
                                             actor.position[1] - self.cameraPosition[1], 
                                             actor.size[0] - PRAM.BOX_FUDGE*2, 
                                             actor.size[1]))
        return
    
    
    
    
    