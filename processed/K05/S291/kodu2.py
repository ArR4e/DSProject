import string
from random import choice

def suurväike(sõna):
    uus_sõna = ""
    uus_märk = choice(string.punctuation)
    for täht in sõna:
        if täht.isupper():
            uus_täht = täht.lower()
            uus_sõna += uus_täht
        elif täht.islower():
            uus_täht = täht.upper()
            uus_sõna += uus_täht
        elif täht in string.punctuation:
                märgid = täht.replace(täht, uus_märk)
                uus_sõna += märgid
        else:
            uus_sõna += " "
    return uus_sõna
        