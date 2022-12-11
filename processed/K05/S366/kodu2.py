import string
import random 

märgid = string.punctuation
#print(märgid)

def suurväike(sõne):
    asendus = random.choice(märgid)
    for täht in sõne:
        if täht in string.punctuation:
            sõne = sõne.replace(täht, asendus)
    return sõne.swapcase()
    
        
print(suurväike("MinA oleN Tubli!!"))
    