from string import punctuation, ascii_letters
from random import randint

def suurväike(fraas):
    tulemus = ""
    r_punkt = randint(0,31)
    for symbol in fraas:
        if symbol in ascii_letters:
            if symbol.islower() == True:
                tulemus += symbol.upper()
            else:
                tulemus += symbol.lower()
        elif symbol in punctuation:
            tulemus += punctuation[r_punkt]
        elif symbol == " ":
            tulemus += " "
    return tulemus
