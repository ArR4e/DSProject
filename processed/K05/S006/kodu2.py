import string
import random

def suurväike(sõne):
    vahetus = sõne.swapcase()
    sümbol = random.choice(string.punctuation)
    uus = ""
    for täht in vahetus:
        if täht in string.punctuation:
            täht = sümbol
            uus += täht
        else:
            täht = täht
            uus += täht
    return uus


    