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
    
    '''
     1) render background.
     2) render lower tiles 
     3) render mid tiles
     4) render actors
     5) render upper tiles
    '''
    def render(self, gameScene):
        self.renderScenery(gameScene.sceneryWrapper)
        if type(gameScene) is GameLevel:
            self.renderTiles(gameScene.layoutWrapper)
        self.renderActors(gameScene.actorsWrapper)
        if type(gameScene) is GameLevel:
            self.renderTiles(gameScene.layoutWrapper, False, False, True)
    
    def renderTiles(self, layoutWrapper, lower = True, mid = True, upper = False):
        for x in range(layoutWrapper.size[0]):
            for y in range(layoutWrapper.size[1]):
                tile = layoutWrapper.layout[x][y]
                location = UTIL.calcPixFromTile((y,x))
                if lower:
                    if tile.lower != '':
                        self.screen.blit(layoutWrapper.tileDict[tile.lower], location)
                if mid:
                    if tile.mid != '':
                        self.screen.blit(layoutWrapper.tileDict[tile.mid], location)
                if upper:
                    if tile.upper != '':                    
                        self.screen.blit(layoutWrapper.tileDict[tile.upper], location)
                
        
            
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
                                 pygame.Rect(actor.position[0]+PRAM.BOX_FUDGE, actor.position[1], 
                                             actor.size[0] - PRAM.BOX_FUDGE*2, actor.size[1]))
        return
    
    