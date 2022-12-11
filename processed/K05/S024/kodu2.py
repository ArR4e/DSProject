import string
import random


def suurväike(sõne):
    uus_sõne =""
    juhuslik_sümbol = random.choice(string.punctuation)
    for tähemärk in sõne:
        if (tähemärk.isupper()) == True:
            uus_sõne += (tähemärk.lower())
        elif (tähemärk.islower()) == True:
            uus_sõne += (tähemärk.upper())
        elif (tähemärk.isspace()) == True:
            uus_sõne += tähemärk
        elif tähemärk in string.punctuation:
            sümboli_muutus = tähemärk.replace(tähemärk, juhuslik_sümbol)
            uus_sõne += sümboli_muutus    
    return uus_sõne



