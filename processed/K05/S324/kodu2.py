import random
import string

def suurväike(sõne):
    uus_sõne = ""
    sümbol = random.choice(string.punctuation)
    for täht in sõne:
        if täht in string.punctuation:
            uus_sõne = uus_sõne + sümbol
        elif täht == täht.lower():
            uus_täht = täht.upper()
            uus_sõne = uus_sõne + uus_täht
        else:
            uus_täht = täht.lower()
            uus_sõne = uus_sõne + uus_täht
    return uus_sõne