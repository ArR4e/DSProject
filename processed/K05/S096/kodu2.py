# Suured väikeseks ja väikesed suureks

import random
import string

def suurväike(tekst):
    tekst = tekst.swapcase()
    tähemärk = random.choice(string.punctuation)
    for i in tekst:
        if i in string.punctuation:
            tekst = tekst.replace(i, tähemärk)
    return tekst

print(suurväike("MinA ,  & oleN Tubli!!"))