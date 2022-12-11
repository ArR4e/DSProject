import string
import random
import re
def suurväike(sõne):
    a = random.choice(string.punctuation)
    for i in list(sõne):
        if i in string.punctuation:
            sõne = sõne.replace(i, a)
    return sõne.swapcase()
print(suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut."))