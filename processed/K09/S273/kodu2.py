# funktsioon ajab ette antud järjendi elemendid segamini

from random import randint
from copy import copy

def minu_shuffle(järjend):
    n = 0
    järjend2 = copy(järjend)
    b = []
    for element in järjend:
        while True:
            a = randint(0, len(järjend))
            if a != len(järjend):
                if a in b:
                    continue
                if a not in b:
                    järjend[n] = järjend2[a]
                    b.append(a)
                    n += 1
                    break
            if a == len(järjend):
                continue

#minu_shuffle([1,2,3,4,5,6])