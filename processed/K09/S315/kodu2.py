from random import randint
from copy import *

def minu_shuffle(järjend):
    olemas = []
    i = 0
    uus = copy(järjend)
    while i <= len(järjend)-1:
        juhuslik = randint(0, len(järjend)-1)
        if juhuslik in olemas:
            continue
        olemas += [juhuslik]
        järjend[i] = uus[juhuslik]
        i += 1
