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
from parameters import BOX_FUDGE

'''
Class which renders images to the screen
@param screen
'''
class Renderer():
    def __init__(self, screen):
        self.screen = screen
        
        #explicit declaration of class fields
        self.camera = None
        self.cameraTile= (0,0)
        self.cameraOffset = (0,0)
        self.cameraPosition = (0,0)
        
        self.levelData = None
        self.lowerTiles = []
        self.upperTiles = []
        self.backgrounds = []
        self.foregrounds = []
        self.actors = []
        
        #for rendering changed tiles, keeps track of rendered tiles
        #indexed by their (x,y) coordinate pair
        self.renderedLowerTiles = {} 
        self.renderedUpperTiles = {} 
        
        self.actorsDict = {} #reference to image files
        self.lowerTileMap = None #image file
        self.upperTileMap = None#image file

        self.renderQueue = []

    def loadAssets(self, levelData):
        self.levelData = levelData #TODO may not need this reference
        self.lowerTiles = levelData.lowerTiles
        self.upperTiles = levelData.upperTiles
        self.backgrounds = levelData.backgrounds
        self.foregrounds = levelData.foregrounds
        self.actors = levelData.actors
        
        self.actorDict = {} #Load actor images
        for actor in self.actors:
            if type(actor) is StaticSprite: #TODO this will be type Sprite or similar
                if self.actorDict.get(actor.image) == None:
                    self.actorDict[actor.image] = pygame.image.load(actor.path+actor.image).convert_alpha()
        
#         for sprite in scenery: #MAY NOT USE SCENERY
#             if type(sprite) is StaticSprite:
#                 if imageDict.get(sprite.image) == None:
#                     imageDict[sprite.image] = pygame.image.load(sprite.path+sprite.image).convert()

        for background in self.backgrounds:
            if background.alpha == True:
                background.image = pygame.image.load(background.filePath).convert_alpha()
            else:
                background.image = pygame.image.load(background.filePath).convert()

        for foreground in self.foregrounds:
            if foreground.alpha == True:
                foreground.image = pygame.image.load(foreground.filePath).convert_alpha()
            else:
                foreground.image = pygame.image.load(foreground.filePath).convert()     
                
        self.lowerTileMap = pygame.image.load(levelData.lowerTileMap.filePath).convert()
        self.upperTileMap = pygame.image.load(levelData.upperTileMap.filePath).convert()
                    
#     def render(self, gameScene):
#         if type(gameScene) is GameLevel:
#             self.cameraTile = gameScene.gameCamera.getTile()
#             self.cameraOffset = gameScene.gameCamera.getOffset()
#             self.cameraPosition = gameScene.gameCamera.getPosition()
#             moveFlag = gameScene.gameCamera.moveFlag
#             if moveFlag == True:
#                 self.renderAllPanorama(gameScene.sceneryWrapper.background, gameScene.sceneryWrapper.imageDict, self.cameraTile, self.cameraOffset)
#                 self.renderAllLowerTile(gameScene.layoutWrapper, self.cameraTile, self.cameraOffset)
#                 self.renderAllActors(gameScene.actorsWrapper)
#                 self.renderAllUpperTile(gameScene.layoutWrapper, self.cameraTile, self.cameraOffset)                
#                 self.renderAllPanorama(gameScene.sceneryWrapper.foreground, gameScene.sceneryWrapper.imageDict, self.cameraTile, self.cameraOffset)                                
#             else:
#                 self.renderChangedPanorama(gameScene.renderQueue, gameScene.sceneryWrapper.background, gameScene.sceneryWrapper.imageDict, self.cameraTile, self.cameraOffset)
#                 self.renderChangedLowerTile(gameScene.renderQueue, gameScene.layoutWrapper, self.cameraTile, self.cameraOffset)                
#                 self.renderChangedActors(gameScene.actorsWrapper)
#                 self.renderChangedUpperTile(gameScene.renderQueue, gameScene.layoutWrapper, self.cameraTile, self.cameraOffset)                 
#                 self.renderChangedPanorama(gameScene.renderQueue, gameScene.sceneryWrapper.foreground, gameScene.sceneryWrapper.imageDict, self.cameraTile, self.cameraOffset)                   
#             gameScene.renderQueue.clear()
#             gameScene.gameCamera.moveFlag = False       
#         else:
#             pass #work on menu rendering    

    #this will just render game levels - create a seperate method for menus, and perhaps cutscenes
    def render(self):
#         self.cameraTile = gameScene.gameCamera.getTile()
#         self.cameraOffset = gameScene.gameCamera.getOffset()
#         self.cameraPosition = gameScene.gameCamera.getPosition()
#         moveFlag = gameScene.gameCamera.moveFlag
        self.cameraTile= self.camera.tile
        self.cameraOffset = self.camera.offset
        self.cameraPosition = self.camera.position

        if len(self.lowerTiles)>0: #quick hack to make sure a level is loaded
            if self.camera.moveFlag == True:
                self.renderAllPanorama(BG = True)
                self.renderAllLowerTile()
                self.renderAllActors()
                self.renderAllUpperTile()                
                self.renderAllPanorama(BG = False)                                
            else:
                self.renderChangedPanorama(BG = True)
                self.renderChangedLowerTile()                
                self.renderChangedActors()
                self.renderChangedUpperTile()                 
                self.renderChangedPanorama(BG = False)                   
            self.renderQueue.clear()
            self.renderedLowerTiles.clear()
            self.renderedUpperTiles.clear()
            self.camera.moveFlag = False       

#     def renderAllLowerTile(self, layoutWrapper, tileOffset, pixelOffset):
    def renderAllLowerTile(self):
        for y in range(PRAM.DISPLAY_TILE_HEIGHT):
            yOffset = y * PRAM.TILESIZE - self.cameraOffset[1]
            for x in range(PRAM.DISPLAY_TILE_WIDTH):
                tile = self.lowerTiles[y + self.cameraTile[1]][x + self.cameraTile[0]]
                if tile[0] != -1: #-1 is blank
                    xOffset = x* PRAM.TILESIZE - self.cameraOffset[0]
                    self.screen.blit(self.lowerTileMap, 
                                     (xOffset, yOffset), #screen position
                                     (tile[0], #tileMap x crop position
                                      tile[1], #tileMap y crop position
                                     PRAM.TILESIZE, #tilemap  width
                                     PRAM.TILESIZE)) #tilemap height
                    
#     def renderAllUpperTile(self, layoutWrapper, tileOffset, pixelOffset):
    def renderAllUpperTile(self):
        for y in range(PRAM.DISPLAY_TILE_HEIGHT):
            yOffset = y * PRAM.TILESIZE - self.cameraOffset[1]
            for x in range(PRAM.DISPLAY_TILE_WIDTH):
                tile = self.upperTiles[y + self.cameraTile[1]][x + self.cameraTile[0]]
                if tile[0] != -1:
                    xOffset = x* PRAM.TILESIZE - self.cameraOffset[0]
                    self.screen.blit(self.upperTileMap, 
                                     (xOffset, yOffset), #screen position
                                     (tile[0], #tileMap x crop position
                                      tile[1], #tileMap y crop position
                                     PRAM.TILESIZE, #tileMap width
                                     PRAM.TILESIZE)) #tileMap height
 
 

#     def renderAllUpperTile(self, layoutWrapper, tileOffset, pixelOffset):
#         for y in range(PRAM.DISPLAY_TILE_HEIGHT):
#             yOffset = y * PRAM.TILESIZE - pixelOffset[1]
#             for x in range(PRAM.DISPLAY_TILE_WIDTH):
#                 tile = layoutWrapper.layout[y + tileOffset[1]][x + tileOffset[0]]
#                 if tile.upper != '':
#                     xOffset = x* PRAM.TILESIZE - pixelOffset[0]
#                     self.screen.blit(layoutWrapper.tileDict[tile.upper], (xOffset, yOffset))

#     def renderChangedLowerTile(self, renderQueue, layoutWrapper, tileOffset, pixelOffset):
#         for box in renderQueue:
#             xRange = (box[0]//PRAM.TILESIZE, box[1]//PRAM.TILESIZE)
#             yRange = (box[2]//PRAM.TILESIZE, box[3]//PRAM.TILESIZE)
#             
#             for x in range(xRange[0], xRange[1]):
#                 for y in range(yRange[0], yRange[1]):
#                     tile = layoutWrapper.layout[y][x]
#                     if tile.changed == False and tile.lower !='':
#                         self.screen.blit(layoutWrapper.tileDict[tile.lower], 
#                                          ((x - tileOffset[0]) * PRAM.TILESIZE  - pixelOffset[0],
#                                          (y - tileOffset[1]) * PRAM.TILESIZE  - pixelOffset[1]))
#                     tile.changed = True

#     self.renderChangedLowerTile(gameScene.renderQueue, gameScene.layoutWrapper, self.cameraTile, self.cameraOffset) 
#     def renderChangedLowerTile(self, renderQueue, layoutWrapper, tileOffset, pixelOffset):
    def renderChangedLowerTile(self):
        for box in self.renderQueue:
            xRange = (box[0]//PRAM.TILESIZE, box[1]//PRAM.TILESIZE)
            yRange = (box[2]//PRAM.TILESIZE, box[3]//PRAM.TILESIZE)
            for x in range(xRange[0], xRange[1]):
                for y in range(yRange[0], yRange[1]):
                    tile = self.lowerTiles[y][x]
                    if self.renderedLowerTiles.get((y,x)) != True and tile[0] != -1:
                        self.screen.blit(self.lowerTileMap,
                                         ((x - self.cameraTile[0]) * PRAM.TILESIZE  - self.cameraOffset[0], #x screen position
                                          (y - self.cameraTile[1]) * PRAM.TILESIZE  - self.cameraOffset[1]), #y screen position
                                         (tile[0], 
                                          tile[1], 
                                         PRAM.TILESIZE, 
                                         PRAM.TILESIZE)) #blit one tile
                        self.renderedLowerTiles[(x,y)] = True

#     def renderChangedUpperTile(self, renderQueue, layoutWrapper, tileOffset, pixelOffset):
    def renderChangedUpperTile(self):
        for box in self.renderQueue:
            xRange = (box[0]//PRAM.TILESIZE, box[1]//PRAM.TILESIZE)
            yRange = (box[2]//PRAM.TILESIZE, box[3]//PRAM.TILESIZE)
            for x in range(xRange[0], xRange[1]):
                for y in range(yRange[0], yRange[1]):
                    tile = self.upperTiles[y][x]
                    if self.renderedUpperTiles.get((y,x)) != True and tile[0] !=-1:
                        self.screen.blit(self.upperTileMap, 
                                         ((x - self.cameraTile[0]) * PRAM.TILESIZE  - self.cameraOffset[0],
                                         (y - self.cameraTile[1]) * PRAM.TILESIZE  - self.cameraOffset[1]),
                                         (tile[0],
                                          tile[1],
                                          PRAM.TILESIZE,
                                          PRAM.TILESIZE))
                        self.renderedUpperTiles[(x,y)] = True
                        

#     def renderAllPanorama(self, images, imageDict, tileOffset, pixelOffset):
#         screenOffset = (tileOffset[0]*PRAM.TILESIZE + pixelOffset[0], 
#                         tileOffset[1]*PRAM.TILESIZE + pixelOffset[1])
#         for fg in images:
#             imageOffset = (screenOffset[0]*fg.scrolling[0][0]//fg.scrolling[0][1]%fg.imageSize[0], 
#                            screenOffset[1]*fg.scrolling[1][0]//fg.scrolling[1][1]%fg.imageSize[1])
#             for vs in fg.visibleSections: #vs = (left edge, right edge, top edge, bottom edge)
#                 
#                 #check if visible portion of background is on screen
#                 if (vs[0] < screenOffset[0] + PRAM.DISPLAY_WIDTH 
#                     and vs[1]> screenOffset[0] 
#                     and vs[2] < screenOffset[1] + PRAM.DISPLAY_HEIGHT 
#                     and vs[3]> screenOffset[1]):
#                     
#                     #find boundaries of image
#                     if vs[0] <= screenOffset[0]:
#                         xOffset = 0
#                     else:
#                         xOffset = vs[0] - screenOffset[0]
#                 
#                     if vs[2] <= screenOffset[1]:
#                         yOffset = 0
#                     else:
#                         yOffset = vs[2]- screenOffset[1]
# 
#                     #calculate size of image square to blit  
#                     xRange = vs[1] - screenOffset[0] - xOffset                      
#                     if xRange + xOffset > PRAM.DISPLAY_WIDTH:
#                         xRange = PRAM.DISPLAY_WIDTH - xOffset
# 
#                     yRange = vs[3] - screenOffset[1] - yOffset
#                     if yRange + yOffset > PRAM.DISPLAY_HEIGHT:
#                         yRange = PRAM.DISPLAY_HEIGHT - yOffset
#                         
#                     currentXrange = xRange #size of block of image to blit
#                     currentYrange = yRange
#                     currentScreenPos = [xOffset,yOffset] #absolute screen position to blit to
#                     
#                     currentCropX = (imageOffset[0] + xOffset)%fg.imageSize[0] #position of image to blit from
#                     currentCropY = (imageOffset[1] + yOffset)%fg.imageSize[1]
#                     keepGoing = True
#                     shiftX = False
#                     shiftY = False
#                     
#                     while keepGoing:
#                         if currentCropX + currentXrange > fg.imageSize[0]:
#                             currentXrange = fg.imageSize[0] - currentCropX  
#                             shiftX = True
#                         if currentCropY + currentYrange > fg.imageSize[1]:
#                             currentYrange = fg.imageSize[1] - currentCropY
#                             shiftY = True
# 
#                         self.screen.blit(imageDict[fg.image], 
#                                          currentScreenPos,
#                                         (currentCropX, currentCropY, currentXrange, currentYrange)) 
#                                                                  
#                         #blit across the X direction first, then shift down the Y and reset the X  
#                         if shiftX:
#                             currentScreenPos = [currentScreenPos[0] + currentXrange, currentScreenPos[1]]
#                             currentCropX = (currentCropX + currentXrange) % fg.imageSize[0]
#                             currentXrange = xRange - currentXrange
#                             shiftX = False
#                         elif shiftY:
#                             currentScreenPos = [xOffset, currentScreenPos[1] + currentYrange]
#                             currentCropX = (imageOffset[0] + xOffset)%fg.imageSize[0]
#                             currentXrange = xRange
#                             currentCropY = (currentCropY + currentYrange) % fg.imageSize[1]
#                             currentYrange = yRange - currentYrange                                                
#                             shiftY = False    
#                         else:
#                             keepGoing = False #you have blitted the entire visible section


#     self.renderAllPanorama(gameScene.sceneryWrapper.background, gameScene.sceneryWrapper.imageDict, self.cameraTile, self.cameraOffset)
#     def renderAllPanorama(self, images, imageDict, tileOffset, pixelOffset):
    def renderAllPanorama(self, BG = True): #if BG render backgrounds, else foregrounds
        screenOffset = (self.cameraTile[0]*PRAM.TILESIZE + self.cameraOffset[0], 
                        self.cameraTile[1]*PRAM.TILESIZE + self.cameraOffset[1])
        if BG:
            images = self.backgrounds
        else:
            images = self.foregrounds
        for fg in images:
            imageOffset = (screenOffset[0]*fg.scrolling[0][0]//fg.scrolling[0][1]%fg.pxSize[0], 
                           screenOffset[1]*fg.scrolling[1][0]//fg.scrolling[1][1]%fg.pxSize[1])
            for vs in fg.visibleSections: #vs = (left edge, right edge, top edge, bottom edge)
                
                #check if visible portion of background is on screen
                if (vs[0] < screenOffset[0] + PRAM.DISPLAY_WIDTH 
                    and vs[1]> screenOffset[0] 
                    and vs[2] < screenOffset[1] + PRAM.DISPLAY_HEIGHT 
                    and vs[3]> screenOffset[1]):
                    
                    #find boundaries of image
                    if vs[0] <= screenOffset[0]:
                        xOffset = 0
                    else:
                        xOffset = vs[0] - screenOffset[0]
                
                    if vs[2] <= screenOffset[1]:
                        yOffset = 0
                    else:
                        yOffset = vs[2]- screenOffset[1]

                    #calculate size of image square to blit  
                    xRange = vs[1] - screenOffset[0] - xOffset                      
                    if xRange + xOffset > PRAM.DISPLAY_WIDTH:
                        xRange = PRAM.DISPLAY_WIDTH - xOffset

                    yRange = vs[3] - screenOffset[1] - yOffset
                    if yRange + yOffset > PRAM.DISPLAY_HEIGHT:
                        yRange = PRAM.DISPLAY_HEIGHT - yOffset
                        
                    currentXrange = xRange #size of block of image to blit
                    currentYrange = yRange
                    currentScreenPos = [xOffset,yOffset] #absolute screen position to blit to
                    
                    currentCropX = (imageOffset[0] + xOffset)%fg.pxSize[0] #position of image to blit from
                    currentCropY = (imageOffset[1] + yOffset)%fg.pxSize[1]
                    keepGoing = True
                    shiftX = False
                    shiftY = False
                    
                    while keepGoing:
                        if currentCropX + currentXrange > fg.pxSize[0]:
                            currentXrange = fg.pxSize[0] - currentCropX  
                            shiftX = True
                        if currentCropY + currentYrange > fg.pxSize[1]:
                            currentYrange = fg.pxSize[1] - currentCropY
                            shiftY = True

                        self.screen.blit(fg.image, 
                                         currentScreenPos,
                                        (currentCropX, currentCropY, currentXrange, currentYrange)) 
                                                                 
                        #blit across the X direction first, then shift down the Y and reset the X  
                        if shiftX:
                            currentScreenPos = [currentScreenPos[0] + currentXrange, currentScreenPos[1]]
                            currentCropX = (currentCropX + currentXrange) % fg.pxSize[0]
                            currentXrange = xRange - currentXrange
                            shiftX = False
                        elif shiftY:
                            currentScreenPos = [xOffset, currentScreenPos[1] + currentYrange]
                            currentCropX = (imageOffset[0] + xOffset)%fg.pxSize[0]
                            currentXrange = xRange
                            currentCropY = (currentCropY + currentYrange) % fg.pxSize[1]
                            currentYrange = yRange - currentYrange                                                
                            shiftY = False    
                        else:
                            keepGoing = False #you have blitted the entire visible section

#     def renderChangedPanorama(self, renderQueue, images, imageDict, tileOffset, pixelOffset):
    def renderChangedPanorama(self, BG = True):
        if BG:
            images = self.backgrounds
        else:
            images = self.foregrounds
        
        for fg in images:
            for box in self.renderQueue:
                for vs in fg.visibleSections:
                    
                    #Check to see if this renderBox is within a visible section of the foreground
                    if vs[0] <= box[1] and vs[1]>= box[0] and vs[2] <= box[3] and vs[3] >= box[2]:
                        visibleBox = list(box)
                        if vs[0] > box[0]:
                            visibleBox[0] = vs[0]
                        if vs[1] < box[1]:
                            visibleBox[1] = vs[1]
                        if vs[2] > box[2]:
                            visibleBox[2] = vs[2]
                        if vs[3] < box[3]:
                            visibleBox[3] = vs[3]        
                                                                                                    
                        startScreenPos = (visibleBox[0] - (self.cameraTile[0]*PRAM.TILESIZE)  - self.cameraOffset[0], 
                                          visibleBox[2] - (self.cameraTile[1]*PRAM.TILESIZE)  - self.cameraOffset[1])
                        
                        startCropX = ((self.cameraTile[0]*PRAM.TILESIZE + self.cameraOffset[0])
                                      * fg.scrolling[0][0]
                                      // fg.scrolling[0][1] 
                                      + startScreenPos[0])
                        startCropX = startCropX % fg.pxSize[0]
                          
                        startCropY = ((self.cameraTile[1]*PRAM.TILESIZE + self.cameraOffset[1])
                                      * fg.scrolling[1][0]
                                      // fg.scrolling[1][1] 
                                      + startScreenPos[1])
                        startCropY = startCropY % fg.pxSize[1]
                                        
                        currentScreenPos = startScreenPos
                        currentCropX =  startCropX
                        currentCropY = startCropY
                        imageSizeX = visibleBox[1] - visibleBox[0] 
                        imageSizeY = visibleBox[3] - visibleBox[2]
                        
                        keepGoing = True
                        shiftX = False
                        shiftY = False
                        
                        #check to see if you are at the boundries of the image, and need to tile it
                        while keepGoing:
                            if currentCropX + imageSizeX > fg.pxSize[0]:
                                imageSizeX = fg.pxSize[0] - currentCropX
                                shiftX = True
                            if currentCropY + imageSizeY > fg.pxSize[1]:
                                imageSizeY = fg.pxSize[1] - currentCropY
                                shiftY = True
                                                    
                            self.screen.blit(fg.image, 
                                             currentScreenPos,
                                            (currentCropX,  #image x
                                            currentCropY, #image y                                 
                                              imageSizeX, #image x width crop
                                              imageSizeY)) #image y height crop   
                            
                            #blit across the X direction first, then shift down the Y and reset the X  
                            if shiftX:
                                currentScreenPos = [currentScreenPos[0] + imageSizeX, currentScreenPos[1]]
                                currentCropX = (currentCropX + imageSizeX) % fg.pxSize[0]
                                imageSizeX = visibleBox[1] - visibleBox[0] - imageSizeX
                                shiftX = False
                            elif shiftY:
                                currentScreenPos = [startScreenPos[0], currentScreenPos[1] + imageSizeY]
                                currentCropX = startCropX
                                imageSizeX = visibleBox[1] - visibleBox[0]
                                currentCropY = (currentCropY + imageSizeY) % imageSizeY
                                imageSizeY = visibleBox[3] - visibleBox[2] - imageSizeY                                                
                                shiftY = False    
                            else:
                                keepGoing = False #you have blitted the entire visible section

#     def renderChangedPanorama(self, renderQueue, images, imageDict, tileOffset, pixelOffset):
#         for fg in images:
#             for box in renderQueue:
#                 for vs in fg.visibleSections:
#                     
#                     #Check to see if this renderBox is within a visible section of the foreground
#                     if vs[0] <= box[1] and vs[1]>= box[0] and vs[2] <= box[3] and vs[3] >= box[2]:
#                         visibleBox = list(box)
#                         if vs[0] > box[0]:
#                             visibleBox[0] = vs[0]
#                         if vs[1] < box[1]:
#                             visibleBox[1] = vs[1]
#                         if vs[2] > box[2]:
#                             visibleBox[2] = vs[2]
#                         if vs[3] < box[3]:
#                             visibleBox[3] = vs[3]        
#                                                                                                     
#                         startScreenPos = (visibleBox[0] - (tileOffset[0]*PRAM.TILESIZE)  - pixelOffset[0], 
#                                           visibleBox[2] - (tileOffset[1]*PRAM.TILESIZE)  - pixelOffset[1])
#                         
#                         startCropX = ((tileOffset[0]*PRAM.TILESIZE + pixelOffset[0])
#                                       * fg.scrolling[0][0]
#                                       // fg.scrolling[0][1] 
#                                       + startScreenPos[0])
#                         startCropX = startCropX % fg.imageSize[0]
#                           
#                         startCropY = ((tileOffset[1]*PRAM.TILESIZE + pixelOffset[1])
#                                       * fg.scrolling[1][0]
#                                       // fg.scrolling[1][1] 
#                                       + startScreenPos[1])
#                         startCropY = startCropY % fg.imageSize[1]
#                                         
#                         currentScreenPos = startScreenPos
#                         currentCropX =  startCropX
#                         currentCropY = startCropY
#                         imageSizeX = visibleBox[1] - visibleBox[0] 
#                         imageSizeY = visibleBox[3] - visibleBox[2]
#                         
#                         keepGoing = True
#                         shiftX = False
#                         shiftY = False
#                         
#                         #check to see if you are at the boundries of the image, and need to tile it
#                         while keepGoing:
#                             if currentCropX + imageSizeX > fg.imageSize[0]:
#                                 imageSizeX = fg.imageSize[0] - currentCropX
#                                 shiftX = True
#                             if currentCropY + imageSizeY > fg.imageSize[1]:
#                                 imageSizeY = fg.imageSize[1] - currentCropY
#                                 shiftY = True
#                                                     
#                             self.screen.blit(imageDict[fg.image], 
#                                              currentScreenPos,
#                                             (currentCropX,  #image x
#                                             currentCropY, #image y                                 
#                                               imageSizeX, #image x width crop
#                                               imageSizeY)) #image y height crop   
#                             
#                             #blit across the X direction first, then shift down the Y and reset the X  
#                             if shiftX:
#                                 currentScreenPos = [currentScreenPos[0] + imageSizeX, currentScreenPos[1]]
#                                 currentCropX = (currentCropX + imageSizeX) % fg.imageSize[0]
#                                 imageSizeX = visibleBox[1] - visibleBox[0] - imageSizeX
#                                 shiftX = False
#                             elif shiftY:
#                                 currentScreenPos = [startScreenPos[0], currentScreenPos[1] + imageSizeY]
#                                 currentCropX = startCropX
#                                 imageSizeX = visibleBox[1] - visibleBox[0]
#                                 currentCropY = (currentCropY + imageSizeY) % imageSizeY
#                                 imageSizeY = visibleBox[3] - visibleBox[2] - imageSizeY                                                
#                                 shiftY = False    
#                             else:
#                                 keepGoing = False #you have blitted the entire visible section

    #TODO - calculate if the actor is onscreen
#     def renderAllActors(self, actorsWrapper):
    def renderAllActors(self):
        for actor in self.actors:
            if type(actor) is SimpleBox:
                pygame.draw.rect(self.screen, actor.color, 
                                 pygame.Rect(actor.position[0]+PRAM.BOX_FUDGE - self.cameraPosition[0], 
                                             actor.position[1] - self.cameraPosition[1], 
                                             actor.size[0] - PRAM.BOX_FUDGE*2, 
                                             actor.size[1]))
            actor.changed = False
        return
    
    #TODO 
#     def renderChangedActors(self, actorsWrapper):
    def renderChangedActors(self):
        for actor in self.actors:
            if actor.changed == True:
                if type(actor) is SimpleBox:
                    pygame.draw.rect(self.screen, actor.color, 
                                     pygame.Rect(actor.position[0]+PRAM.BOX_FUDGE - self.cameraPosition[0], 
                                                 actor.position[1] - self.cameraPosition[1], 
                                                 actor.size[0] - PRAM.BOX_FUDGE*2, 
                                                 actor.size[1]))
                actor.changed = False
        return
    

#     #TODO - calculate if the actor is onscreen
#     def renderAllActors(self, actorsWrapper):
#         for actor in actorsWrapper.actors:
#             if type(actor) is SimpleBox:
#                 pygame.draw.rect(self.screen, actor.color, 
#                                  pygame.Rect(actor.position[0]+PRAM.BOX_FUDGE - self.cameraPosition[0], 
#                                              actor.position[1] - self.cameraPosition[1], 
#                                              actor.size[0] - PRAM.BOX_FUDGE*2, 
#                                              actor.size[1]))
#             actor.changed = False
#         return
#     
#     #TODO 
#     def renderChangedActors(self, actorsWrapper):
#         for actor in actorsWrapper.actors:
#             if actor.changed == True:
#                 if type(actor) is SimpleBox:
#                     pygame.draw.rect(self.screen, actor.color, 
#                                      pygame.Rect(actor.position[0]+PRAM.BOX_FUDGE - self.cameraPosition[0], 
#                                                  actor.position[1] - self.cameraPosition[1], 
#                                                  actor.size[0] - PRAM.BOX_FUDGE*2, 
#                                                  actor.size[1]))
#                 actor.changed = False
#         return

#TODO - scenery should be part of actors?                  
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
    Based on start and end position, and actor size, add a bounding box to the 
        renderQueue (in pixels) for a section of the gameLevel that needs to be
        rendered on the render changes call 
    '''
    def addRenderBox(self, size, origin, destination, direction):
        if direction == PRAM.UP:
            minx = origin[0]
            miny = destination[1]
            maxx = destination[0] + size[0]
            maxy = origin[1] + size[1]
        elif direction == PRAM.DOWN:
            minx = origin[0]
            miny = origin[1]
            maxx = destination[0] + size[0]
            maxy = destination[1] + size[1]
        elif direction == PRAM.LEFT:
            minx = destination[0] 
            miny = origin[1]
            maxx = origin[0] + size[0]
            maxy = destination[1] + size[1]
        else: #right
            minx = origin[0]
            miny = origin[1]
            maxx = destination[0] + size[0]
            maxy = destination[1] + size[1]
        
        mapSizeX = self.levelData.size[1] * PRAM.TILESIZE
        mapSizeY = self.levelData.size[0] * PRAM.TILESIZE
        
        #get the entire tile
        minx = minx - (minx % PRAM.TILESIZE)
        miny = miny - (miny % PRAM.TILESIZE)
        maxx = (maxx//PRAM.TILESIZE + 1)*PRAM.TILESIZE
        maxy = (maxy//PRAM.TILESIZE + 1)*PRAM.TILESIZE        
             
        if minx<0:
            minx = 0
        if miny<0:
            miny = 0
        if maxx > mapSizeX:
            maxx = mapSizeX 
        if maxy > mapSizeY:
            maxy = mapSizeY            
                
        self.renderQueue.append((minx, maxx, miny, maxy))
    
    
    