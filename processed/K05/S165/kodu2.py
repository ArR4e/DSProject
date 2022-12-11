import string
from random import choice

def suurväike(sõne):
    
    uus_sõne = []
    sõne = list(sõne)
    i = -1
    random_sümbol = choice(string.punctuation)
    
    
    for sümbol in sõne:
        i = i + 1
        
        # Muudan sümboli ära vastavalt vajadusele
        if sümbol.islower() == True:
            sümbol = sümbol.upper()
        elif sümbol.isupper() == True:
            sümbol = sümbol.lower()
        elif sümbol in string.punctuation:
            sümbol = sümbol.replace(sümbol, random_sümbol )
        
        # Lisan uuendatud sümboli uute sõnesse
        uus_sõne.insert(i, sümbol)
    
    uus_sõne = "".join(uus_sõne)
    return uus_sõne
    



        




