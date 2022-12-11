#kodu2 - suurväike
import string
from random import choice
def suurväike(sõna):
    vahemärk = choice(string.punctuation)
    for i in sõna:
        if i in string.punctuation:
            sõna = sõna.replace(i, vahemärk)
    sõna = sõna.swapcase()
    return sõna







