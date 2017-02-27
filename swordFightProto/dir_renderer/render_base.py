'''
Created on Feb 25, 2017

@author: Robert
'''

#base class to be extended 
class RenderBase():
    def __init__(self, screen, components):
        self.screen = screen
        self.components = components
    
    
    #iterate through every component
    def render(self):
        for component in self.components:
            self.renderFeature(component)
    
    #define this in the subclass
    def renderFeature(self, component):
        pass 