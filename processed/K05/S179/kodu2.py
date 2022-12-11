import string
import random


def suurväike(sõne):
    
    parandus = ""
    kirjavahemärk = random.choice(string.punctuation)
    
    for täht in sõne:
        if täht in string.punctuation:
            parandus += kirjavahemärk
        elif täht == täht.upper():
            parandus += täht.lower()
        elif täht == täht.lower():
            parandus += täht.upper()
        elif täht == täht.isnumeric():
            parandus += täht
        elif täht == "":
            break
    return(parandus)


            