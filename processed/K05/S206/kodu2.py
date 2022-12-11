from string import *
from random import *
def suurväike(sõne):
    pikkus = len(sõne)
    uus = ""
    märk = punctuation[randint(1, len(punctuation))]
    for i in range(pikkus):
        if sõne[i].isupper():
            uus += sõne[i].lower()
        elif sõne[i].islower():
            uus += sõne[i].upper()
        elif sõne[i] == " ":
            uus += " "
        elif sõne[i] in punctuation:
            uus += märk
        
    return uus

