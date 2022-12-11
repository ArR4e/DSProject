from string import punctuation
from random import choice

def suurväike(b):
    b=b.swapcase()
    for i in b:
        if i in punctuation:
            b=b.replace(i,"?")
    b=b.replace("?",choice(punctuation))
    return b
    
        