import string
from random import*

def suurväike(sõne):
    arv = randint(0, len(string.punctuation) - 1 )
    märk = (string.punctuation[arv])
    uus_sõne = ""
    for i in sõne:
        if i.isupper():
            uus_sõne += i.lower()
        elif i.islower():
            uus_sõne += i.upper()
        elif i == " ":
            uus_sõne += i
        else:
            uus_sõne += märk
    return uus_sõne
print((suurväike("Tallinn-Haapsalu-Viljandi-Tartu-Narva")))
            
            
        

