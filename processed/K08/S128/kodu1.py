#Bingo!
from random import sample
def bingo():
    arvud1_10 = [1,2,3]
    while 1 in arvud1_10 and 2 in arvud1_10 and 3 in arvud1_10:
        arvud1_10 = sample(range(1,11),3)
    arvud11_20 = sample(range(11,21),2)
    return arvud1_10 + arvud11_20
print(bingo())

