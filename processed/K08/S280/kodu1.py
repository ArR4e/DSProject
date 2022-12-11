# 1. Bingo! / RP
from random import sample

def bingo():
    numbrid = [1,2,3]
    while 1 in numbrid and 2 in numbrid and 3 in numbrid:
        numbrid = []
        numbrid.extend(sample(range(1,11), 3))
        numbrid.extend(sample(range(11,21), 2))
    return numbrid

print(bingo())