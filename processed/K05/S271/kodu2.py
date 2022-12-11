import string
from random import randint

def suurväike(sõne):
    uus = ''
    valik = list(string.punctuation)[randint(0, 31)]
    for sümbol in sõne:
        if sümbol == ' ':
            uus +=' '
        elif sümbol in string.punctuation:
            uus += valik 
        if sümbol.islower():
            uus += sümbol.upper()
        elif sümbol.isupper():
            uus += sümbol.lower()
    return uus
    
    