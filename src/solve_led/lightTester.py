'''
Created on 1 Mar 2018

@author: robbie
skeleton code from Assignment3: hints
'''
class lightTester:
    lights = None
     
    def __init__(self,N):
         
        self.lights = [[False]*N for i in range(N)]
        self.count=0
    
    def turn_on(self,tuple):
        for i in range (int(tuple[0]),int(tuple[2])+1):
            for j in range(int(tuple[1]),int(tuple[3])+1):
                if not self.lights[i][j]:
                    self.lights[i][j]=True
                    self.count+=1
                    
    def turn_off(self,tuple):
        for i in range (int(tuple[0]),int(tuple[2])+1):
            for j in range(int(tuple[1]),int(tuple[3])+1):
                if self.lights[i][j]:
                    self.lights[i][j]=True
                    self.count-=1
                    
    def switch(self,tuple):
        for i in range (int(tuple[0]),int(tuple[2])+1):
            for j in range(int(tuple[1]),int(tuple[3])+1):
                if lights[i][j]:
                    lights[i][j] = False
                    self.count-=1
                else:
                    lights[i][j] = True
                    self.count+=1
         
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
