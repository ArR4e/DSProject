from random import*

def bingo():
    arvud1 = sample(range(1,11),3)
    while True:
        if 1 in arvud1 and 2 in arvud1 and 3 in arvud1:
            arvud1 = sample(range(1,11),3)
        else:
            break
    arvud2 = sample(range(11,21),2)
    return arvud1+arvud2

print(bingo())