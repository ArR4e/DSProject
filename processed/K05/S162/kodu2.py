import string
import random
def suurväike(sõne):
    sõne=sõne.swapcase()
    x=random.choice(string.punctuation)
    for i in sõne:
        if i in string.punctuation:
            sõne=sõne.replace(i,x)
    return sõne
            

print(suurväike("aJ?/ ///"))