import string
from random import randrange

def suurväike(tekst):
    uus_märk = string.punctuation[randrange(0, len(string.punctuation))]
    sona = ""
    i = 0
    while i < len(tekst):
        taht = tekst[i]
        if taht.isalpha():
            if taht.isupper():
                sona += taht.lower()
            else:
                sona += taht.upper()
        elif taht == " ":
            sona += " "
        else:
            sona += uus_märk
        i += 1
    return sona

