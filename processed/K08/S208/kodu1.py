import random
def bingo():
    jrj = [6]
    while sum(jrj) == 6:  
        jrj = random.sample([*range(1,11)], 3)
        jrj2 = random.sample([*range(11,21)], 2)
    return jrj + jrj2