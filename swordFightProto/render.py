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
                self.renderChangedBackground(gameScene.renderQueue, gameScene.layoutWrapper, gameScene.sceneryWrapper, self.cameraTile, self.cameraOffset)
                self.renderChangedLowerTile(gameScene.renderQueue, gameScene.layoutWrapper, self.cameraTile, self.cameraOffset)                
                self.renderActors(gameScene.actorsWrapper)
                self.renderChangedUpperTile(gameScene.renderQueue, gameScene.layoutWrapper, self.cameraTile, self.cameraOffset)                 
                self.renderChangedForeground(gameScene.renderQueue, gameScene.layoutWrapper, gameScene.sceneryWrapper, self.cameraTile, self.cameraOffset)                   
            gameScene.renderQueue.clear()
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

    #TODO: will change this to rendering full swatches at a time?, based on bounding boxes
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

    #TODO if tile.background = True
    def renderChangedBackground(self, renderQueue, layoutWrapper, sceneryWrapper, tileOffset, pixelOffset):
        for bg in sceneryWrapper.background:
            for box in renderQueue:
                #TODO - WIP, tiling background is trickier, may need to blit in chunks
#                 patches = [] #an array of patches to blit render
#                 startx = (box[0])//bg.scrollFactorX
#                 endx = startx + (box[1] - box[0])
#                 if endx > bg.size[0]: #need to split here
#                     startx2 = 
                screenpos = (box[0] - (tileOffset[0] * PRAM.TILESIZE)  - pixelOffset[0], box[2] - (tileOffset[1] * PRAM.TILESIZE)  - pixelOffset[1])
                self.screen.blit(sceneryWrapper.imageDict[bg.image], 
                                 screenpos,
                                ((tileOffset[0] * PRAM.TILESIZE + pixelOffset[0])//bg.scrollFactorX + screenpos[0],  #image x
                                (tileOffset[1] * PRAM.TILESIZE + pixelOffset[1])//bg.scrollFactorY + screenpos[1], #image y                                 
                                  box[1] - box[0], #image x width crop
                                  box[3] - box[2])) #image y height crop               

    def renderChangedLowerTile(self, renderQueue, layoutWrapper, tileOffset, pixelOffset):
        for box in renderQueue:
            xRange = (box[0]//PRAM.TILESIZE, box[1]//PRAM.TILESIZE)
            yRange = (box[2]//PRAM.TILESIZE, box[3]//PRAM.TILESIZE)
            
            for x in range(xRange[0], xRange[1]):
                for y in range(yRange[0], yRange[1]):
                    tile = layoutWrapper.layout[y][x]
                    if tile.changed == False and tile.lower !='':
                        self.screen.blit(layoutWrapper.tileDict[tile.lower], 
                                         ((x - tileOffset[0]) * PRAM.TILESIZE  - pixelOffset[0],
                                         (y - tileOffset[1]) * PRAM.TILESIZE  - pixelOffset[1]))
                    tile.changed = True

    #TODO - check to see if
    def renderChangedActors(self, actorsWrapper):
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
    
    def renderChangedUpperTile(self, renderQueue, layoutWrapper, tileOffset, pixelOffset):
        for box in renderQueue:
            xRange = (box[0]//PRAM.TILESIZE, box[1]//PRAM.TILESIZE)
            yRange = (box[2]//PRAM.TILESIZE, box[3]//PRAM.TILESIZE)
            
            for x in range(xRange[0], xRange[1]):
                for y in range(yRange[0], yRange[1]):
                    tile = layoutWrapper.layout[y][x]
                    if tile.changed == True and tile.upper !='':
                        self.screen.blit(layoutWrapper.tileDict[tile.upper], 
                                         ((x - tileOffset[0]) * PRAM.TILESIZE  - pixelOffset[0],
                                         (y - tileOffset[1]) * PRAM.TILESIZE  - pixelOffset[1]))
                    tile.changed = False

    #TODO - tile.forground = True (how to do this with chunks?  
    def renderChangedForeground(self, renderQueue, layoutWrapper, sceneryWrapper, tileOffset, pixelOffset):
        for fg in sceneryWrapper.foreground:
            for box in renderQueue:
                #TODO - WIP, tiling background is trickier, may need to blit in chunks
#                 patches = [] #an array of patches to blit render
#                 startx = (box[0])//bg.scrollFactorX
#                 endx = startx + (box[1] - box[0])
#                 if endx > bg.size[0]: #need to split here
#                     startx2 = 
                screenpos = (box[0] - (tileOffset[0] * PRAM.TILESIZE)  - pixelOffset[0], box[2] - (tileOffset[1] * PRAM.TILESIZE)  - pixelOffset[1])
                imagecropx = (tileOffset[0] * PRAM.TILESIZE + pixelOffset[0])*fg.scrollSpeed + screenpos[0]
                imagecropx = imagecropx % fg.size[0]
                imagecropy = (tileOffset[1] * PRAM.TILESIZE + pixelOffset[1])*fg.scrollSpeed + screenpos[1]
                imagecropy = imagecropy % fg.size[1]
                self.screen.blit(sceneryWrapper.imageDict[fg.image], 
                                 screenpos,
                                (imagecropx,  #image x
                                imagecropy, #image y                                 
                                  box[1] - box[0], #image x width crop
                                  box[3] - box[2])) #image y height crop      

                  
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
    
    
    
    
    