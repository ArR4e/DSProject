import string
import random

pun = random.choice(string.punctuation)
sõna = ("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut.")
def suurväike(x):
    vahetatud = sõna.swapcase()
    for täht in sõna:
        if täht in string.punctuation:
            vahetatud = vahetatud.replace(täht, pun)

        else:
            continue
    return vahetatud
print(suurväike(sõna))