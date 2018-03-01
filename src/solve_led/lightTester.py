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
        self.size=N
        
    def turn_on(self,tuple):
        for i in range (max(int(tuple[0]),0),min(int(tuple[2])+1,self.size)):
            for j in range(max(int(tuple[1]),0),min(int(tuple[3])+1,self.size)):
                if not self.lights[i][j]:
                    self.lights[i][j]=True
                    self.count+=1
                    
    def turn_off(self,tuple):
        for i in range (max(int(tuple[0]),0),min(int(tuple[2])+1,self.size)):
            for j in range(max(int(tuple[1]),0),min(int(tuple[3])+1,self.size)):
                if self.lights[i][j]:
                    self.lights[i][j]=False
                    self.count-=1
                    
    def switch(self,tuple):
        for i in range (max(int(tuple[0]),0),min(int(tuple[2])+1,self.size)):
            for j in range(max(int(tuple[1]),0),min(int(tuple[3])+1,self.size)):
                if self.lights[i][j]:
                    self.lights[i][j] = False
                    self.count-=1
                else:
                    self.lights[i][j] = True
                    self.count+=1
         
    def apply(self,cmd):
        if cmd[0] == 'turn on':
            self.turn_on(cmd[1:])
        elif cmd[0]=='turn off':
            self.turn_off(cmd[1:])
        elif cmd[0]=='switch':
            self.switch(cmd[1:])
