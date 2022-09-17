class Titandex:
    def __init__(self,name,height,strength,winning_streak):
        self.n=name
        self.h=height
        self.s=strength
        self.w=winning_streak
    def TitanvsScout(self):
        scoutn=input('enter scout name')
        scouts=int(input('enter scout strength'))
        if(scouts<self.s):
            print('winner = ',self.n)
            self.w=self.w+1
        if(scouts>self.s):
            print('winner = ',scoutn)
            self.w=0
        if(scouts==self.s):
            print('draw')
            self.w=0
        print(self.w)
    def TitanvsTitan(self):
        titann=input('enter titan name')
        titans=int(input('enter titan strength'))
        if(titann!=self.n):
            if(titans<self.s):
                print('winner = ',self.n)
                self.w=self.w+1
            if(titans>self.s):
                print('winner = ',titann)
                self.w=0
            if(titans==self.s):
                print('draw')
                self=0    
        else:
            print('select different titan') 
            
titan=Titandex(input(),int(input()),int(input()),0)
numopp=int(input('enter num of opp'))
while(numopp!=0):
    opp=input('select opponent')
    if(opp=='Scout'):
        Titandex.TitanvsScout(titan)
    if(opp=='Titan'):
        Titandex.TitanvsTitan(titan)
        numopp=numopp-1
print(titan.w)
