import string
import random

def split(kraam):
    return list(kraam)

def suurväike(sõne):
    sõne = str(sõne)
    sõne = sõne.swapcase()
    j = string.punctuation
    j = split(j)
    j = random.choice(j)
    for i in sõne:
        if i in string.punctuation:
            sõne = sõne.replace(i,j)
    return sõne
            
