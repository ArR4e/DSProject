import string
import random

def suurväike(sõne):
    sõne = list(sõne)
    kirjavahemärk = random.choice(string.punctuation)
    for i in range(len(sõne)):
        if sõne[i].isupper() == True:
            sõne[i] = sõne[i].lower()
        elif sõne[i].islower() == True:
            sõne[i] = sõne[i].upper()
        elif sõne[i] in string.punctuation:
            sõne[i] = kirjavahemärk
    sõne = "".join(sõne)
    return(sõne)