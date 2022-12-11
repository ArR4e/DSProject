#alustasin 23.10.2021 (21:47)
from random import *

def minu_shuffle(jarjend):
    for i in range(len(jarjend)):
        juhuslik_arv = randint(0, i)
        jarjend[i], jarjend[juhuslik_arv] = jarjend[juhuslik_arv], jarjend[i]