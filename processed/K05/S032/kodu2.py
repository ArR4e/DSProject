import string
import random


def suurväike(sõne):
    tulemus = ""
    sümbol = random.choice(string.punctuation)
    print(sümbol)
    for s in sõne:
        if s.isalpha():
            tulemus += s.swapcase()
        elif s in string.punctuation:
            tulemus += s.replace(s,sümbol)
        else:
            tulemus += s
    return tulemus

#print(suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut."))