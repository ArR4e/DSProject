from random import sample

def bingo():
    while True:
        järjend1 = []
        järjend2 = []
        järjend1 = sample(range(1, 11), 3)
        if sum(järjend1) != 6:
            järjend2 += sample(range(11, 21), 2)
            tulemusjärjend = järjend1 + järjend2
        else:
            continue
        return tulemusjärjend

#print(bingo())