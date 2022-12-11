import string
from random import randrange

sõne = input()
uussõne = string.punctuation[randrange(0, len(string.punctuation))]

def suurväike(sõne):
    if sõne.isalpha():
        print(sõne)
    
    if sõne.isupper():
        print(sõne.lower())
        
    elif sõne.lower():
        print(sõne.upper())
            
    elif sõne is string.punctuation:
        print(uussõne)

suurväike(sõne)
    
    
