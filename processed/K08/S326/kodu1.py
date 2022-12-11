from random import sample
def bingo():
    jär = []
    while True:
        esimesed = sample(range(1, 11), 3)
        if [1, 2, 3] == sorted(esimesed):
            continue
        else:
            jär += esimesed
            break
    jär += sample(range(11, 21), 2)
    return jär