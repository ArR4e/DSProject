import string
from random import randint

def suurväike(a):
    sõna = ""
    märk = string.punctuation[randint(0, len(string.punctuation) -1)]
    for el in a:
        if el in string.punctuation:
            el = märk
        if el.isupper():
           sõna += el.lower()
        else:
           sõna+= el.upper()
    return sõna

print(suurväike("MinA .oleN? Tubli!"))