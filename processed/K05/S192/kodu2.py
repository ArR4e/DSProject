import string
import random
def suurväike(sõne):
    vahetatud = sõne.swapcase()
    pnkt = random.choice(string.punctuation)
    for i in string.punctuation:
        vahetatud = vahetatud.replace(i, pnkt)
    return vahetatud