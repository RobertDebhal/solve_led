#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 1 Mar 2018

@author: robbie
'''
import unittest
from lightTester import *
#from solve_led.lightTester import *
#from solve_led.console_script import *

class TestLightTesterClass(unittest.TestCase):
    def test_turn_on(self):
        lights=lightTester(1000) #create lights object 1000*1000
        lights.turn_on((0,0,0,999)) #turn on row 0
        lights.turn_on((200,0,200,999)) #turn on row 200
        lights.turn_on((400,0,400,999)) #turn on row 400
        lights.turn_on((600,0,600,999)) #turn on row 600
        lights.turn_on((800,0,800,999)) #turn on row 800
        lights.turn_on((800,0,800,999)) #turn on row 800 again. should do nothing.
        self.assertTrue(lights.count==5000) #check count. Should be 5000 
    
    def test_turn_off(self):
        lights=lightTester(1000) #create lights object 1000*1000
        lights.turn_on((0,0,0,999)) #turn on row 0
        lights.turn_on((200,0,200,999)) #turn on row 200
        lights.turn_on((400,0,400,999)) #turn on row 400
        lights.turn_on((600,0,600,999)) #turn on row 600
        lights.turn_on((800,0,800,999)) #turn on row 800
        lights.turn_off((400,0,400,999)) #turn off row 400
        lights.turn_off((600,0,600,999)) #turn off row 600
        lights.turn_off((600,0,600,999)) #turn off row 600 again. Should do nothing.
        self.assertTrue(lights.count==3000) #check count. Should be 3000 
    
    def test_switch(self):
        lights=lightTester(1000) #create lights object 1000*1000
        lights.turn_on((0,0,0,999)) #turn on row 0
        lights.turn_on((200,0,200,999)) #turn on row 200
        lights.turn_on((400,0,400,999)) #turn on row 400
        lights.turn_on((600,0,600,999)) #turn on row 600
        lights.turn_on((800,0,800,999)) #turn on row 800
        lights.turn_off((400,0,400,999)) #turn off row 400
        lights.turn_off((600,0,600,999)) #turn off row 600
        lights.turn_off((600,0,600,999)) #turn off row 600 again. Should do nothing.
        lights.switch((0,0,999,999)) #switch all lights. count should be 997,000
        self.assertTrue(lights.count==997000) #check count. Should be 997,000 
        
        
    def test_apply(self):
        lights = lightTester(1000)
        lights.apply(('turn on', '51', '51', '100', '100')) #count should now be 2,500
        lights.apply(('switch' , '0','0', '999' ,'999')) #count should now be 997,500
        lights.apply(('turn off', '900', '0', '999', '999')) #count should now be 897,500
        lights.apply(('turn on', '900','-10','999','999')) #should correct for light out of range.
                                                   #count should now be 997,500
        lights.apply(('turn off', '900', '0', '1000', '1000')) #should correct for light out of range.
                                                   #count should now be 897,500
        self.assertTrue(lights.count==897500)
        
class ConsoleScriptTest:
    def check_file(self):
        """
        Also should check at this stage for incorrect commands to ignore
        self.Assert(fileCheck==True) #check for the existence of input file
        """
    
