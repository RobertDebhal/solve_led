'''
Created on 1 Mar 2018

@author: robbie
skeleton code from Assignmnt3: hints
'''

from lightTester import lightTester
import parse_file, sys

def main(filename):
    #source: https://stackoverflow.com/questions/40753946/python-setup-tools-console-scripts-with-arguments 
    arg1, arg2 = sys.argv[1], sys.argv[2]
    print(arg1, arg2)
    
    start=time.time()
    instructions = parse_file.ParseFile(filename)
    print(time.time()-start)
    
    lights = lightTester(int(instructions.lines[0]))
    
    for i in range(1,len(instructions.lines)):
        lights.apply(instructions.lines[i])
    
    print("#occupied:",lights.count()) 
    
if __name__ == '__main__':
    main('commands.txt')