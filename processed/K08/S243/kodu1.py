# 1. Bingo!

from random import sample

def bingo():
    while True:
        numbrid=sample(range(1, 11), 3)
        if 1 in numbrid and 2 in numbrid and 3 in numbrid:
            continue
        break
    viimased=sample(range(11, 21), 2)
    numbrid+=viimased
    
    return numbrid
