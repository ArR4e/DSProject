import string
import random

def suurväike(sõne):
    uus = ""
    märk = random.choice(string.punctuation)
    for täht in sõne:
        if täht in string.punctuation:
            täht = märk
            uus += täht
        elif täht == täht.upper():
            täht = täht.lower()
            uus += täht
        elif täht == täht.lower():
            täht = täht.upper()
            uus += täht
    return uus
            