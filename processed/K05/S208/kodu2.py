import string 
import random
def suurväike(sõne):
    sõne = sõne.swapcase()
    tõlk = str.maketrans(string.punctuation, random.choice(string.punctuation) * len(string.punctuation))
    sõne = sõne.translate(tõlk)
    return sõne
