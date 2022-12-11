import string
import random

def suurväike(sõne):
    uussõne = ""
    kirjavahemärk = random.choice(string.punctuation)
    for i in sõne:
        if i in string.punctuation:
            uussõne += kirjavahemärk
        else:
            uussõne += i.swapcase()
    return uussõne
            