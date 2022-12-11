import string
from random import randint

def suurväike(sõne):
    sümbolid = []
    sümbolid[:0] = string.punctuation
    sümbol = sümbolid[randint(0, len(sümbolid))]
    uus_sõne = ""
    for i in range(len(sõne)):
        if not sõne[i].isalnum() and sõne[i] != " ":
            uus_sõne += sümbol
        elif sõne[i].isupper():
            uus_sõne += sõne[i].lower()
        elif sõne[i].islower():
            uus_sõne += sõne[i].upper()
        else:
            uus_sõne += sõne[i]
            
    return uus_sõne
