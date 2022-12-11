#suured tähed on muudetud väikeseks;
#väikesed tähed on muudetud suureks;
#kõik kirjavahemärkide sümbolid on asendatud mingi ühe ja sama juhusliku kirjavahemärgisümboliga.
import string
from random import randint
punctuation = ["!","#","$","%","&","?","@","~"]

def suurväike(x):
    x2 = ""
    for a in x:
        if (a.isupper()) == True:
            x2 += a.lower()
        elif (a.islower()) == True:
            x2 += a.upper()
        elif (a.isspace()) == True:
            x2 += a
        elif a in string.punctuation:
            i = int(randint(0,len(punctuation)))
            x2 += a.replace(a,punctuation[i])
    return x2

print(suurväike(input("Sup?: ")))
