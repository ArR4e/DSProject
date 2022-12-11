from random import sample, randint
def bingo():
    e=sample(range(1,11),3)
    en=sample(range(11,21),2)
    e[2]=4
    while True:
        if e[0]==e[1] or e[1]==e[2] or e[1]==2:
            e[1]=randint(4,10)
        elif e[0]==e[2]:
            e[0]=randint(4,10)
        else:
            break
    e.extend(en)
    return e

