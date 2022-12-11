import string
from random import randrange
def suurväike(sõna):

    #sumbol = len(sõna)
    x = string.punctuation[randrange(0, len(string.punctuation))]
    i = 0
    summa = ''
    while i < len(sõna):
        if sõna[i].isalpha():
            if sõna[i].isupper():
                summa += sõna[i].lower()
            else:
                summa += sõna[i].upper()
        if sõna[i] in string.punctuation:
            summa += x
        i += 1
    return(summa)
