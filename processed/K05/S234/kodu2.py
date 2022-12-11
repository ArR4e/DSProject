from random import *
import string as s
def suurväike(sõna):
    uus=choice(s.punctuation)
    for a in range(len(sõna)):
        sõna=list(sõna)
        if sõna[a].islower():
            sõna[a]=sõna[a].upper()
        elif sõna[a].isupper():
            sõna[a]=sõna[a].lower()
        else:
            if sõna[a] in s.punctuation:
                sõna[a]=uus
    sõna="".join(sõna)
    return(sõna)