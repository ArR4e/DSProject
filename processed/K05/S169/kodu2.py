import random
import string

def suurväike(sõne):
    uussõne = ""
    randmärk = random.choice(string.punctuation)
    for a in sõne:
        if a.isupper() == True:
            a = a.lower()
        elif a.islower() == True:
            a = a.upper()
        elif a == " ":
            a = a
        else:
            a = randmärk
            
        uussõne += uussõne.join(a)
    return uussõne
        
print(suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut."))