'''
Created on Feb 27, 2017

This module is not yet robust, but creating a unit test mainly to test
the framework

@author: Robert
'''
import unittest
import os

from scenery import *

class Test(unittest.TestCase):

    def setUp(self):
        self.solidBackground=SolidBackground((0, 0, 0))
        imagePath = os.path.realpath('')+'\\dir_image\\'
        image='testsprite.png'
        pixelLocation = (20,20)
        self.staticSprite=StaticSprite(imagePath+image,pixelLocation)

### SolidBackground() ###
    def test_colorChange(self):
        self.assertEqual(self.solidBackground.color, (0,0,0))
        self.assertEqual(self.solidBackground.colorChange((1,1,1)), True)
        self.assertEqual(self.solidBackground.color, (1,1,1))

    def tearDown(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()