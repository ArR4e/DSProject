from random import randrange
import string

def suurväike(sõna):
    uussõna = ""
    for a in sõna:
        if (a.isupper()) == True:
            uussõna+=(a.lower())
        elif (a.islower()) == True:
            uussõna+=(a.upper())
        elif a in string.punctuation:
            uussõna += string.punctuation[randrange(0,len(string.punctuation))]
        elif (a.isspace()) == True:
            uussõna+=a
    return uussõna