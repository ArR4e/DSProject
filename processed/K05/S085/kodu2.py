import string
import random
def suurväike(sõne):
    sõne = sõne.swapcase()
    punkt = string.punctuation
    a = random.choice(punkt)
    for c in sõne:
        if c in punkt:
            sõne = sõne.replace(c, a)
    return sõne