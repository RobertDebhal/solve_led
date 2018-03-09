'''
Created on 1 Mar 2018

@author: robbie
'''
import urllib.request as url, re
import sys 
class ParseFile:
    def __init__(self,filename,type='local'):
        
        self.bad_file=False
        self.bad_url=False
        try:
            self.file = open(filename,'r')
        except FileNotFoundError:
            type='https'
            self.bad_file=True
            
            
        valid = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        
        if type=='local':
            self.file = open(filename,'r')
            self.lines = self.file.readlines()
            for i in range(len(self.lines)):
                if valid.match(self.lines[i]):
                    self.lines[i]=(valid.match(self.lines[i]).group(1),
                                   valid.match(self.lines[i]).group(2),
                                   valid.match(self.lines[i]).group(3),
                                   valid.match(self.lines[i]).group(4),
                                   valid.match(self.lines[i]).group(5))
        else:
            try:
                self.file = url.urlopen(filename)
                self.lines = self.file.readlines()
                for i in range(len(self.lines)):
                    self.lines[i] = self.lines[i].decode('utf-8')
                    if valid.match(self.lines[i]):
                        self.lines[i]=(valid.match(self.lines[i]).group(1),
                                       valid.match(self.lines[i]).group(2),
                                       valid.match(self.lines[i]).group(3),
                                       valid.match(self.lines[i]).group(4),
                                       valid.match(self.lines[i]).group(5))
            except ValueError:
                print("Please type a valid URL or filename")
                self.bad_url=True
            except url.HTTPError:
                self.bad_url=True
                
            
            
            
    def iterate(self):
        for i in self.lines[1:10]:
            print(i) 

def main():
    file = ParseFile('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt','https')
    file.iterate()

if __name__ =='__main__':
    main()  