#RPS algorithm:
import random

    
Pscore=0
Cchoice=None
Pchoice=None
results=None
run=0
won=0
lose=0
draw=0

def Compplays(Cchoice):
    global results, Cscore, Pscore, choices, List, run
    choices={0:1,1:2,2:0}
    if Cchoice==None:
        Cchoice=1
    else:
        if results=='Lose':
            Cchoice=choices.get(List[-1])
        elif results=='Draw':
            Cchoice=random.randint(0,2)
        elif results=='Win':
            Cchoice=choices(Cchoice)
    run+=1
    return Cchoice



List=[]
List.append(Pchoice)
Cmove=Compplays(Cchoice)