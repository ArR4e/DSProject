import random

def bingo():
    arvud1 = random.sample(range(1, 10), 3)
    arvud2 = random.sample(range(11, 20), 2)
    arvud3 = arvud1 + arvud2
    print(arvud3)
    

    
    
bingo()
    
