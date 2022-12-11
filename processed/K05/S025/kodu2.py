import string
import random

def suurväike(sõne):
    sümbolid = string.punctuation
    suvaline_sümbol = random.choice(string.punctuation)
    uus_sõne = ''
    for a in sõne:
        if (a.isupper()) == True:
            uus_sõne += (a.lower())
        elif (a.islower()) == True:
            uus_sõne += (a.upper())
        elif (a.isspace()) == True:
            uus_sõne += a
        elif a in sümbolid:
            uus_sõne += suvaline_sümbol
    return uus_sõne