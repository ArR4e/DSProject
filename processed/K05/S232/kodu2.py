import random
import string
kirjavahemärgid = string.punctuation
asendus = random.choice(kirjavahemärgid)

def suurväike(sõne):
    for element in sõne:
        if element in kirjavahemärgid:
            sõne = sõne.replace(element, asendus)
        else:
            continue
    return sõne.swapcase()

suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut.")