import string
import random

def suurväike(sõne):
    x= random.randint(0,31)
    uus = ''
    for a in sõne:
        if a.islower() == True:
            uus = uus + a.upper()
        elif a.isupper() == True:
            uus = uus + a.lower()
        elif a in string.punctuation:
            uus = uus + string.punctuation[x]
        else:
            uus = uus + ' '
    return uus
print(suurväike(input("sisesta sõne")))

