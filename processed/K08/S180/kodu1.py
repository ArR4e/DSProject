from random import sample

def bingo():
    
    arvud = []
        
    arvud = arvud + sample(range(1, 11), 3)
    arvud = arvud + sample(range(11, 21), 2)
    
    if 1 in arvud and 2 in arvud and 3 in arvud:
        arvud = bingo()
        return arvud
    else:
        return arvud
    
print(bingo())