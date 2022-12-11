import string
from random import*

def suurväike(sõne):
    b = randint(0, len(string.punctuation)-1) #returns random
    asendus = string.punctuation[b]
    a = "" #a=sõne
    for i in sõne:
        if i in string.punctuation:
            a = a + asendus
        else:
            a = a + i
    return a.swapcase() #suured väikseks ja vice versa