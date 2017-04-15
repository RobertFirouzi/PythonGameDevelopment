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
    def render(self, gameScene):
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
        screenOffset = (tileOffset[0]*PRAM.TILESIZE + pixelOffset[0], tileOffset[1]*PRAM.TILESIZE + pixelOffset[1])
        for bg in sceneryWrapper.background:
            imageOffset = (screenOffset[0]//bg.scrollFactorX, screenOffset[1]// bg.scrollFactorY)
            for vs in bg.visibleSections: #vs = (left edge, right edge, top edge, bottom edge)
                #check if visible portion of background is on screen
                if (vs[0] < screenOffset[0] + PRAM.DISPLAY_WIDTH or vs[1]> screenOffset[0]) and (
                    vs[2] < screenOffset[1] + PRAM.DISPLAY_HEIGHT or vs[3]> screenOffset[1] ):
                    
                    #find boundaries of image
                    if vs[0] <= screenOffset[0]:
                        xOffset = 0
                    else:
                        xOffset = vs[0] - screenOffset[0]
                
                    if vs[2] <= screenOffset[1]:
                        yOffset = 0
                    else:
                        yOffset = vs[2]- screenOffset[1]
                        
                    if vs[1] - vs[0] + xOffset > PRAM.DISPLAY_WIDTH:
                        xRange = PRAM.DISPLAY_WIDTH - xOffset
                    else:
                        xRange = vs[1] - vs[0]

                    #calculate size of image square to blit
                    if vs[3] - vs[2]+ yOffset > PRAM.DISPLAY_HEIGHT:
                        yRange = PRAM.DISPLAY_HEIGHT - yOffset
                    else:
                        yRange = vs[3] - vs[2]
                
                    self.screen.blit(sceneryWrapper.imageDict[bg.image],
                                     (xOffset, yOffset), 
                                    (imageOffset[0] + xOffset, imageOffset[1] + yOffset, xRange, yRange))

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

    def renderChangedBackground(self, renderQueue, layoutWrapper, sceneryWrapper, tileOffset, pixelOffset):
        screenOffset = (tileOffset[0]*PRAM.TILESIZE + pixelOffset[0], tileOffset[1]*PRAM.TILESIZE + pixelOffset[1])        
        for bg in sceneryWrapper.background:
            for box in renderQueue:
                #check if the section being rendered has any background image
                isBackground = False
                for vs in bg.visibleSections:
                    if vs[0] <= box[1] and vs[1]>= box[0] and vs[2] <= box[3] and vs[3] >= box[2]:
                        isBackground = True
                        break
                    
                if isBackground:
                    screenpos = (box[0] - (tileOffset[0] * PRAM.TILESIZE)  - pixelOffset[0], box[2] - (tileOffset[1] * PRAM.TILESIZE)  - pixelOffset[1])
                    self.screen.blit(sceneryWrapper.imageDict[bg.image], 
                                     screenpos, 
                                     (screenOffset[0]//bg.scrollFactorX + screenpos[0], 
                                      screenOffset[1]//bg.scrollFactorY + screenpos[1], 
                                       box[1] - box[0], 
                                       box[3] - box[2]))               

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

    #TODO - only blit if within a section where foreground = True
    def renderChangedForeground(self, renderQueue, layoutWrapper, sceneryWrapper, tileOffset, pixelOffset):
        for fg in sceneryWrapper.foreground:
            for box in renderQueue:
                startScreenPos = (box[0] - (tileOffset[0] * PRAM.TILESIZE)  - pixelOffset[0], box[2] - (tileOffset[1] * PRAM.TILESIZE)  - pixelOffset[1])
                
                startCropX = (tileOffset[0] * PRAM.TILESIZE + pixelOffset[0])*fg.scrollSpeed + startScreenPos[0]
                startCropX = startCropX % fg.size[0]
                
                startCropY = (tileOffset[1] * PRAM.TILESIZE + pixelOffset[1])*fg.scrollSpeed + startScreenPos[1]
                startCropY = startCropY % fg.size[1]
                                
                currentScreenPos = startScreenPos
                currentCropX =  startCropX
                currentCropY = startCropY
                imageSizeX = box[1] - box[0] 
                imageSizeY = box[3] - box[2]
                
                keepGoing = True
                shiftX = False
                shiftY = False
                while keepGoing:
                    if currentCropX + imageSizeX > fg.size[0]:
                        imageSizeX = fg.size[0] - currentCropX
                        shiftX = True
                    if currentCropY + imageSizeY > fg.size[1]:
                        imageSizeY = fg.size[1] - currentCropY
                        shiftY = True
                                            
                    self.screen.blit(sceneryWrapper.imageDict[fg.image], 
                                     currentScreenPos,
                                    (currentCropX,  #image x
                                    currentCropY, #image y                                 
                                      imageSizeX, #image x width crop
                                      imageSizeY)) #image y height crop   
                    
                    #blit across the X direction first, then shift down the Y and reset the X  
                    if shiftX:
                        currentScreenPos = [currentScreenPos[0] + imageSizeX, currentScreenPos[1]]
                        currentCropX = (currentCropX + imageSizeX) % fg.size[0]
                        imageSizeX = box[1] - box[0] - imageSizeX
                        shiftX = False
                    elif shiftY:
                        currentScreenPos = [startScreenPos[0], currentScreenPos[1] + imageSizeY]
                        currentCropX = startCropX
                        imageSizeX = box[1] - box[0]
                        currentCropY = (currentCropY + imageSizeY) % imageSizeY
                        imageSizeY = box[3] - box[2] - imageSizeY                                                
                        shiftY = False    
                    else:
                        keepGoing = False
                  
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
    
    
    
    
    