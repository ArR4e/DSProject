from string import punctuation
from random import randint
def suurväike(x):
    märk = punctuation[randint(0, 31)]
    for i in x:
        if i in punctuation:
            x = x.replace(i, märk)
    return x.swapcase()
