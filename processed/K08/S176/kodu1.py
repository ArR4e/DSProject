from random import sample
def bingo():
    while True:
        try:
            esimesed = sample(range(1, 11), 3)
            teised = sample(range(11, 21), 2)
        except:
            continue
        else:
            if sorted(esimesed) != [1, 2, 3]:
                break
    return esimesed + teised
