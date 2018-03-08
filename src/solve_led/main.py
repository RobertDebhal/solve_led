'''
Created on 1 Mar 2018

@author: robbie
skeleton code from Assignmnt3: hints
'''

from solve_led.lightTester import lightTester
import solve_led.parse_file as parse_file, sys

def main():
    #source: https://stackoverflow.com/questions/40753946/python-setup-tools-console-scripts-with-arguments 
    arg1, arg2 = sys.argv[1], sys.argv[2]
    if len(sys.argv==2):
        if arg1=='--input'or arg1=='-I':
            instructions = parse_file.ParseFile(arg2)
    
            lights = lightTester(int(instructions.lines[0]))
    
            for i in range(1,len(instructions.lines)):
                lights.apply(instructions.lines[i])
    
            print("#occupied:",lights.count()) 
        else:
            print(arg1+" is not recognised as a valid option")
if __name__ == '__main__':
    main()