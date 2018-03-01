'''
Created on 1 Mar 2018

@author: robbie
skeleton code from Assignment3: hints
'''

class lightsTester:
    lights = None
     
    def __init__(self,N):
         
        self.lights = [[False]*N for i in range(N)]
         
         
    def apply(self,cmd):
        if cmd == 'turn on':
            #switch on
            pass
        elif cmd=='turn off':
            #switch off
            pass
        elif cmd=='switch':
            #switch
            pass
        
    def count(self):
        count=0
        for i in self.lights:
            for j in i:
                if j:
                    count+=1  
        return count
        
    
         
         