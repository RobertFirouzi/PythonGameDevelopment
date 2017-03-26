'''
Created on Feb 25, 2017

@author: Robert
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
    def render(self, gameScene): #TODO - remove need for the branch on gamescene type?
        if type(gameScene) is GameLevel:
            self.cameraTile = gameScene.gameCamera.getTile()
            self.cameraOffset = gameScene.gameCamera.getOffset()
            self.cameraPosition = gameScene.gameCamera.getPosition()
            moveFlag = gameScene.gameCamera.moveFlag
            if moveFlag == True:
                self.renderAllBackground(gameScene.layoutWrapper,gameScene.sceneryWrapper, self.cameraTile, self.cameraOffset)
                self.renderAllLowerTile(gameScene.layoutWrapper, self.cameraTile, self.cameraOffset)
                self.renderAllActors(gameScene.actorsWrapper)
                self.renderAllUpperTile(gameScene.layoutWrapper, self.cameraTile, self.cameraOffset)                
                self.renderAllForeground(gameScene.layoutWrapper,gameScene.sceneryWrapper, self.cameraTile, self.cameraOffset)                                
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


    #note: tileOffset = self.cameraTile, pizelOffset = selt.cameraOffset
    def renderAllBackground(self, layoutWrapper, sceneryWrapper, tileOffset, pixelOffset):
        for bg in sceneryWrapper.background:
            imageOffset = ((tileOffset[0] * PRAM.TILESIZE + pixelOffset[0]) // bg.scrollFactorX, 
                       (tileOffset[1] * PRAM.TILESIZE + pixelOffset[1]) // bg.scrollFactorY)
            for y in range(PRAM.DISPLAY_TILE_HEIGHT):
                yOffset = y * PRAM.TILESIZE
                for x in range(PRAM.DISPLAY_TILE_WIDTH):
                    tile = layoutWrapper.layout[y+tileOffset[1]][x+tileOffset[0]]
                    if tile.background == True:
                        xOffset = x * PRAM.TILESIZE
                        self.screen.blit(sceneryWrapper.imageDict[bg.image],
                                         (xOffset, yOffset), 
                                        (imageOffset[0] + xOffset, imageOffset[1] + yOffset, PRAM.TILESIZE, PRAM.TILESIZE))

    def renderAllLowerTile(self, layoutWrapper, tileOffset, pixelOffset):
        for y in range(PRAM.DISPLAY_TILE_HEIGHT):
            yOffset = y * PRAM.TILESIZE - pixelOffset[1]
            for x in range(PRAM.DISPLAY_TILE_WIDTH):
                tile = layoutWrapper.layout[y + tileOffset[1]][x + tileOffset[0]]
                if tile.lower != '':
                    xOffset = x* PRAM.TILESIZE - pixelOffset[0]
                    self.screen.blit(layoutWrapper.tileDict[tile.lower], (xOffset, yOffset))

    
    #TODO - calculate if the actor is onscreen
    def renderAllActors(self, actorsWrapper):
        for actor in actorsWrapper.actors:
            if type(actor) is SimpleBox:
                pygame.draw.rect(self.screen, actor.color, 
                                 pygame.Rect(actor.position[0]+PRAM.BOX_FUDGE - self.cameraPosition[0], 
                                             actor.position[1] - self.cameraPosition[1], 
                                             actor.size[0] - PRAM.BOX_FUDGE*2, 
                                             actor.size[1]))
            actor.changed = False
        return
    
    def renderAllUpperTile(self, layoutWrapper, tileOffset, pixelOffset):
        for y in range(PRAM.DISPLAY_TILE_HEIGHT):
            yOffset = y * PRAM.TILESIZE - pixelOffset[1]
            for x in range(PRAM.DISPLAY_TILE_WIDTH):
                tile = layoutWrapper.layout[y + tileOffset[1]][x + tileOffset[0]]
                if tile.upper != '':
                    xOffset = x* PRAM.TILESIZE - pixelOffset[0]
                    self.screen.blit(layoutWrapper.tileDict[tile.upper], (xOffset, yOffset))

    def renderAllForeground(self, layoutWrapper, sceneryWrapper, tileOffset, pixelOffset):
        for fg in sceneryWrapper.foreground:
            imageOffset = ((tileOffset[0] * PRAM.TILESIZE + pixelOffset[0]) * fg.scrollSpeed, 
                       (tileOffset[1] * PRAM.TILESIZE + pixelOffset[1]) * fg.scrollSpeed)
            for y in range(PRAM.DISPLAY_TILE_HEIGHT):
                yOffset = y * PRAM.TILESIZE
                for x in range(PRAM.DISPLAY_TILE_WIDTH):
                    tile = layoutWrapper.layout[y+tileOffset[1]][x+tileOffset[0]]
                    if tile.foreground == True:
                        xOffset = x * PRAM.TILESIZE
                        self.screen.blit(sceneryWrapper.imageDict[fg.image],
                                         (xOffset, yOffset), 
                                        ((imageOffset[0] + xOffset) % fg.size[0], 
                                         (imageOffset[1] + yOffset) % fg.size[1], 
                                         PRAM.TILESIZE, PRAM.TILESIZE))

#     def renderChangedBackground(self):
#         pass

    def renderChangedLowerTile(self):
        pass

    def renderChangedActors(self):
        pass 
    
    def renderChangedUpperTile(self):
        pass

#     def renderChangedForeground(self):
#         pass    


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
               
#     '''
#     Render all scenery
#     @param sceneryWrapper
#     '''
#     def renderScenery(self, sceneryWrapper):
#         for feature in sceneryWrapper.scenery:
#             if type(feature) is SolidBackground:
#                 self.screen.fill(feature.color)
#                 
#             elif type(feature) is StaticSprite:
#                 self.screen.blit(sceneryWrapper.imageDict[feature.image], feature.location)
#                 
#             elif type(feature) is SimpleBox:
#                 pygame.draw.rect(self.screen, feature.color, 
#                                  pygame.Rect(feature.position[0], feature.position[1], 
#                                              feature.size[0], feature.size[1]))                
#         return
    
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
    
    
    
    
    