import string
import random

def suurväike(sõne):
    uus_sõne = ""
    x = list(string.punctuation)
    y = random.choice(x)
    for i in sõne:
        if i.islower():
            uus_sõne += i.upper()
        elif i.isupper():
            uus_sõne += i.lower()
        elif i == " ":
            uus_sõne += i
        else:
            uus_sõne += y
    return uus_sõne
 