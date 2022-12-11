import string
import random

def suurväike(a):
    uus=''
    x = random.choice(string.punctuation)
    for täht in a:
        if täht in string.punctuation:
            uus += x
        else:
            uus += täht.swapcase()
        
    return uus