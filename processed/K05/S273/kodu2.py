from random import *
from string import *


def suurväike(sõna):
    muudetudSõna = ""
    for täht in sõna:
        if täht.isupper() == True:
            muudetudSõna += täht.lower()
        elif täht.isupper() == False:
            muudetudSõna += täht.upper()
        if täht in punctuation:
                muudetudSõna += choice(punctuation)
  
    return(muudetudSõna)