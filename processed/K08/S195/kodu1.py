from random import sample

def bingo():
    while True:
        lugeja = 0
        esimesed = sample(range(1, 11), 3)
        for x in range(3):
            if esimesed[x] == 1 or esimesed[x] == 2 or esimesed[x] == 3:
                lugeja += 1
        if lugeja == 3:
            continue
        teised = sample(range(11,21), 2)
        bingonr = esimesed + teised
        print(bingonr)
        break