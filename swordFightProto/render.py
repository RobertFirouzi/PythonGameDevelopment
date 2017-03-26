'''
Created on Feb 25, 2017

@author: Robert
TEST RENDER BRANCH
'''

from actors import SimpleBox
from scenery import StaticSprite, SolidBackground, SceneryWrapper
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
        
        #explicit declaration of class fields
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
    def render(self, gameScene): #TODO - remove need for the branch on gamescene type
        if type(gameScene) is GameLevel:
            self.cameraTile = gameScene.gameCamera.getTile()
            self.cameraOffset = gameScene.gameCamera.getOffset()
            self.cameraPosition = gameScene.gameCamera.getPosition()
            moveFlag = gameScene.gameCamera.moveFlag
#         self.renderScenery(gameScene.sceneryWrapper) # this will probably go away
            if moveFlag == True:
                self.renderTiles(gameScene.layoutWrapper, gameScene.sceneryWrapper)  
                self.renderActors(gameScene.actorsWrapper)
                self.renderTiles(gameScene.layoutWrapper, gameScene.sceneryWrapper, False)
                
            else:
                self.renderChangedBackground(gameScene.backgroundQueue, gameScene.sceneryWrapper)                
                self.renderChangedTiles(gameScene.renderQueue, gameScene.layoutWrapper)
                self.renderActors(gameScene.actorsWrapper)                
                self.renderChangedTiles(gameScene.renderQueue, gameScene.layoutWrapper, False)
                self.renderChangedForeground(gameScene.renderQueue, gameScene.sceneryWrapper)    
            gameScene.renderQueue.clear()
            gameScene.backgroundQueue.clear()
            gameScene.gameCamera.moveFlag = False       
        else:
            pass #work on menu rendering    


    def renderChangedBackground(self, tileQueue, sceneryWrapper = []):
        for tile in tileQueue:
            if tile[0].background == True:
                for br in sceneryWrapper.background:
                    location = UTIL.calcPixFromTile((tile[1][0] - self.cameraTile[0], 
                                                     tile[1][1] - self.cameraTile[1]), 
                                                    -self.cameraOffset[0], 
                                                    -self.cameraOffset[1])
                    backgroundLocation = br.calcBackgroundLocation(location, 
                                                                   (tile[1][0] - self.cameraTile[0],
                                                                    tile[1][1] - self.cameraTile[1]))
                    
                    backgroundCrop = br.calcBackgroundCrop((tile[1][0] - self.cameraTile[0],
                                                            tile[1][1] - self.cameraTile[1]), 
                                                            self.cameraTile, 
                                                            self.cameraOffset)
                    
                    self.screen.blit(sceneryWrapper.imageDict[br.image],
                                     backgroundLocation, 
                                    (backgroundCrop[0], backgroundCrop[1], PRAM.TILESIZE, PRAM.TILESIZE))

    def renderChangedForeground(self, backgroundQueue, sceneryWrapper = []):
        for tile in backgroundQueue:
            if tile[0].foreground == True:
                for fg in sceneryWrapper.foreground:
                    location = UTIL.calcPixFromTile((tile[1][0] - self.cameraTile[0], 
                                                     tile[1][1] - self.cameraTile[1]), 
                                                    -self.cameraOffset[0], 
                                                    -self.cameraOffset[1])
                    foregroundLocation = fg.calcForegroundLocation(location, 
                                                                   (tile[1][0] - self.cameraTile[0],
                                                                    tile[1][1] - self.cameraTile[1]))
                    
                    foregroundCrop = fg.calcForegroundCrop((tile[1][0] - self.cameraTile[0],
                                                            tile[1][1] - self.cameraTile[1]), 
                                                            self.cameraTile, 
                                                            self.cameraOffset)
                    
                    self.screen.blit(sceneryWrapper.imageDict[fg.image],
                                     foregroundLocation, 
                                    (foregroundCrop[0], foregroundCrop[1], PRAM.TILESIZE, PRAM.TILESIZE))
   
    def renderChangedTiles(self, renderQueue, layoutWrapper, lower = True):
        for tile in renderQueue:
            location = UTIL.calcPixFromTile((tile[1][0] - self.cameraTile[0], 
                                             tile[1][1] - self.cameraTile[1]), 
                                            -self.cameraOffset[0], 
                                            -self.cameraOffset[1])
            if lower:
                if tile[0].changed == False: #prevents rendering tiles twice if in queue twice
                    if tile[0].lower != '':
                        self.screen.blit(layoutWrapper.tileDict[tile[0].lower], location)
                    if tile[0].mid != '':
                        self.screen.blit(layoutWrapper.tileDict[tile[0].mid], location)
                tile[0].changed = True
            else:
                if tile[0].changed == True: #prevents rendering tiles twice if in queue twice                
                    if tile[0].upper != '':                    
                        self.screen.blit(layoutWrapper.tileDict[tile[0].upper], location)
                tile[0].changed = False
                  
                   
    def renderTiles(self, layoutWrapper, sceneryWrapper= [], lower = True):
        for y in range(PRAM.DISPLAY_TILE_HEIGHT):
            for x in range(PRAM.DISPLAY_TILE_WIDTH):
                tile = layoutWrapper.layout[y+self.cameraTile[1]][x+self.cameraTile[0]]
                location = UTIL.calcPixFromTile((x,y), -self.cameraOffset[0], -self.cameraOffset[1])
                if lower:
                    if tile.background == True:
                        for br in sceneryWrapper.background:
                            backgroundLocation = br.calcBackgroundLocation(location, (x,y))
                            backgroundCrop = br.calcBackgroundCrop((x,y), self.cameraTile, self.cameraOffset)
                            self.screen.blit(sceneryWrapper.imageDict[br.image],
                                             backgroundLocation, 
                                            (backgroundCrop[0], backgroundCrop[1], PRAM.TILESIZE, PRAM.TILESIZE))
                    if tile.lower != '':
                        self.screen.blit(layoutWrapper.tileDict[tile.lower], location)
                    if tile.mid != '':
                        self.screen.blit(layoutWrapper.tileDict[tile.mid], location)
                else:
                    if tile.upper != '':                    
                        self.screen.blit(layoutWrapper.tileDict[tile.upper], location)
#                     if tile.foreground == True:
                    for fg in sceneryWrapper.foreground:
                        foregroundLocation = fg.calcForegroundLocation(location, (x,y))
                        foregroundCrop = fg.calcForegroundCrop((x,y), self.cameraTile, self.cameraOffset)
                        self.screen.blit(sceneryWrapper.imageDict[fg.image],
                                         foregroundLocation, 
                                        (foregroundCrop[0], foregroundCrop[1], PRAM.TILESIZE, PRAM.TILESIZE))
               
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
            if actor.changed == True:
                if type(actor) is SimpleBox:
                    pygame.draw.rect(self.screen, actor.color, 
                                     pygame.Rect(actor.position[0]+PRAM.BOX_FUDGE - self.cameraPosition[0], 
                                                 actor.position[1] - self.cameraPosition[1], 
                                                 actor.size[0] - PRAM.BOX_FUDGE*2, 
                                                 actor.size[1]))
                actor.changed = False
        return
    
    
    
    
    