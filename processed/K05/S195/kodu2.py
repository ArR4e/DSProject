import string
import random

def suurväike(s6ne):
    punktid = list(string.punctuation)
    out = ""
    for x in s6ne:
        if x in string.punctuation:
            x = random.choice(punktid)
        out = out + x
    return out.swapcase()