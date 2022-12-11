import random
import string


def suurväike(sõne):
    sõne = sõne.swapcase()
    muutus = random.choice(string.punctuation)
    for i in sõne:
        if i in string.punctuation:
            sõne = sõne.replace(i,muutus)
    return sõne

sõne = str(input("Sisesta midagi: "))

print(suurväike(sõne))
