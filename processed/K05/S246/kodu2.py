import random
import string

def suurväike(sõne):
    vastupidi_sõned = sõne.swapcase()
    uus_märk = random.choice(string.punctuation)
    asendus = vastupidi_sõned
    for täht in vastupidi_sõned:
        if täht in string.punctuation:
            asendus = asendus.replace(täht, uus_märk)
    return asendus