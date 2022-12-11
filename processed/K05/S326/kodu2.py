from string import punctuation
from random import choice
def suurväike(t):
    uus = ""
    randchar = choice(punctuation)
    for i in t:
        if (i in punctuation) == True:
          uus += i.replace(i, randchar)
        else:
            uus += i.swapcase()
    return uus

 