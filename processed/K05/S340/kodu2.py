import string
import random

def suurväike(algsõna):
    lõppsõna = ''
    for a in algsõna:
        if (a.isupper()) == True:
            lõppsõna += (a.lower())
        elif (a.islower()) == True:
            lõppsõna += (a.upper())
        elif a in string.punctuation:
            lõppsõna += random.choice(string.punctuation)
    print(lõppsõna)
algsõna = "TeR-ViS"
suurväike(algsõna)