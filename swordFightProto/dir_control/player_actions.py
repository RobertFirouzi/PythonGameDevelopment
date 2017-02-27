'''
Created on Feb 25, 2017

@author: Robert
'''

class ActionBase():
    def __init__(self,params):
        self.params=params
        pass
    
class ActionMove(ActionBase):
    def __init__(self, direction, params=[]):
        super(ActionMove, self).__init__(params)
        self.direction=direction

#performs the default action
class ActionDefault(ActionBase):
    def __init__(self,params=[]):
        super(ActionDefault, self).__init__(params)