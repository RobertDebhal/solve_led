'''
Created on 1 Mar 2018

@author: robbie
skeleton code from Assignment3: hints
'''
class lightTester:
    lights = None
     
    def __init__(self,N):
         
        self.lights = [[False]*N for i in range(N)]
        #consider using count method instead of attribute...
        # lots of unnecessary overhead
        self.size=N
        
    def turn_on(self,tuple):
        for i in range (max(min(int(tuple[0]),int(tuple[2])),0),min(max(int(tuple[2])+1,int(tuple[0])+1),self.size)):
            for j in range(max(min(int(tuple[1]),int(tuple[3])),0),min(max(int(tuple[1])+1,int(tuple[3])+1),self.size)):
                if not self.lights[i][j]:
                    self.lights[i][j]=True
                    
    def turn_off(self,tuple):
        for i in range (max(min(int(tuple[0]),int(tuple[2])),0),min(max(int(tuple[2])+1,int(tuple[0])+1),self.size)):
            for j in range(max(min(int(tuple[1]),int(tuple[3])),0),min(max(int(tuple[1])+1,int(tuple[3])+1),self.size)):
                if self.lights[i][j]:
                    self.lights[i][j]=False
                    
    def switch(self,tuple):
        for i in range (max(min(int(tuple[0]),int(tuple[2])),0),min(max(int(tuple[2])+1,int(tuple[0])+1),self.size)):
            for j in range(max(min(int(tuple[1]),int(tuple[3])),0),min(max(int(tuple[1])+1,int(tuple[3])+1),self.size)):
                if self.lights[i][j]:
                    self.lights[i][j] = False
                else:
                    self.lights[i][j] = True
         
    def apply(self,cmd):
        if cmd[0] == 'turn on':
            self.turn_on(cmd[1:])
        elif cmd[0]=='turn off':
            self.turn_off(cmd[1:])
        elif cmd[0]=='switch':
            self.switch(cmd[1:])

    def count(self):
        count=0
        for i in self.lights:
            for j in i:
                if j:
                    count+=1
        return count