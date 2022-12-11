import string
from random import randint

def suurväike(sõne):
    koht = randint(0, len(string.punctuation)+1)
    märk = string.punctuation[koht]
    
    for täht in sõne:
        if täht in string.punctuation:
            sõne = sõne.replace(täht, märk)
        else:
            continue
            
    return sõne.swapcase()