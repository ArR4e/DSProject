from random import sample

def bingo():
    while True:
        kokku = []
        kokku += sample(range(1,11),3)
        kokku += sample(range(11,21),2)
        if 2 in kokku and not 3 in kokku:
            return kokku
        elif 1 in kokku and not 2 in kokku:
            return kokku
        elif 3 in kokku and not 1 in kokku:
            return kokku
        else:
            continue
