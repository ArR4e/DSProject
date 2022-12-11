from string import punctuation
from random import choice

def suurväike(lause):
    kirjavahemärk = choice(punctuation)
    lause2 = ""
    for i in lause:
        if i in punctuation:
            lause2 += kirjavahemärk
        elif i.isupper():
            lause2 += i.lower()
        elif i.islower():
            lause2 += i.upper()
        else:
            lause2 += " "
    return lause2