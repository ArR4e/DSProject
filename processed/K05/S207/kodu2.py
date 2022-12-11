import string
from random import randint

def suurväike(tekst):
    asendus = string.punctuation[randint(0,31)]
    sõne = ""
    for täht in tekst:
        if täht in string.ascii_lowercase:
            täht = täht.upper()
        elif täht in string.ascii_uppercase:
            täht = täht.lower()
        elif täht in string.punctuation:
            täht = asendus
        sõne = sõne + täht
    return(sõne)