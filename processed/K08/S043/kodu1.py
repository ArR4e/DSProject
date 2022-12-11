from random import sample
from random import randint
def bingo():
    arvud = sample(range(1, 4), 1) + sample(range(4 ,11), 2) + sample(range(11, 21), 2)
    return arvud

print(bingo())
    