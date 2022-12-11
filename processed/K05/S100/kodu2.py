import string
from random import randint

def suurväike(sone):
    uussone = ""
    arv = randint(0, len(string.punctuation)-1)
    mark = string.punctuation[arv]
    for i in sone:
        if i in string.punctuation:
            uussone += mark
        elif i.lower() == i:
            uussone += i.upper()
        else:
            uussone += i.lower()
    return uussone

