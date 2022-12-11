#Suured väikeseks ja väikesed suureks
from random import randint
import string
puncs = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
punc = puncs[randint(0, 31)]

def suurväike(sone):
    sun = ""
    for char in sone:
        if char in string.punctuation:
            sun += punc
        elif char.isupper():
            sun += char.lower()
        elif not char.isupper():
            sun += char.upper()
    return sun
