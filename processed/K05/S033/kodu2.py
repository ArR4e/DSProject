import string
import random

def suurväike(sõne):
    vahetatud = sõne.swapcase()
    juhuslik_märk = random.choice(string.punctuation)
    for märk in vahetatud:
        if märk in string.punctuation:
            global uus_sõne
            uus_sõne = vahetatud.replace(märk, juhuslik_märk)
            vahetatud = uus_sõne
    return uus_sõne
    
