import string
import random


def suurväike (x):
    uus_märk = []
    punctuation_list = list(string.punctuation)
    random.shuffle(punctuation_list)
    random_sümbol= punctuation_list [0]
    for sümbol in x:
        if sümbol in string.punctuation:
            uus_märk.append(random_sümbol)
        elif sümbol.islower():
            uus_märk.append(sümbol.upper())
        elif  sümbol.isupper():
            uus_märk.append(sümbol.lower())
        else:
            uus_märk.append(sümbol)
            
    return "".join(uus_märk)
    
tekst = input ("Palun kirjutage siia oma tekst: ")
print(suurväike(tekst))




