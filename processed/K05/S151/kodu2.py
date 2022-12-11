from random import *
from string import *

def suurväike(sõne):
    uus = ""
    for täht in sõne:
        if (täht.isupper()) == True:
            uus += (täht.lower())
        elif (täht.islower()) == True:
            uus += (täht.upper())
        if (täht.isalpha()) == False:
            uus += choice(punctuation)

    return(uus)

print(suurväike("Apppi KaSS Saaa"))