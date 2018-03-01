'''
Created on 1 Mar 2018

@author: robbie
skeleton code from Assignmnt3: hints
'''

import lightTester

def main(filename,N):
    
    lights = lightTester(N)
    
    instructions = parse_file(filename)
    
    for cmd in instructions:
        lights.apply(cmd)
    
    print("#occupied:",lights.count()) 