from random import sample

def bingo():
    arvud=[]
    
    arvud1=sample(range(1,11),3)
    arvud2=sample(range(11,21),2)
    
    while 1 in arvud1 and 2 in arvud1 and 3 in arvud1:
        arvud1=sample(range(1,11),3)
        
    
    arvud+=arvud1+arvud2
    return arvud

