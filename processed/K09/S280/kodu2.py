# 2. minu_shuffle / RP
from random import *

def minu_shuffle(järjend):
    n = 0
    for el in järjend:
        suva = randint(0, len(järjend)-1)
        vana = järjend[n]
        järjend[n] = järjend[suva]
        järjend[suva] = vana
        n += 1