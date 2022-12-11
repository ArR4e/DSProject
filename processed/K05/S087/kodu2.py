import string
import random

def suurväike (sõne):
    if sõne.upper():
        return uus_sõne
    elif sõne.lower():
        return uus_sõne
    else:
        return random.choice(string.punctuation)

sõne = input("Sisestage lause: ")
uus_sõne = sõne.swapcase()
print ("Sisestatud sõne ümbertehtuna on: ", suurväike (sõne))