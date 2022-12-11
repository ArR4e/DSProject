import random
import string

def suurväike(sõne):
    pikkus = len(sõne)
    sõna = ""
    for i in range(pikkus):
        if sõne[i].islower():
            sõna += str(sõne[i].upper())
        elif sõne[i].isupper():
            sõna += str(sõne[i].lower())               
        else:
            sõna += random.choice(string.punctuation)
    
    return sõna