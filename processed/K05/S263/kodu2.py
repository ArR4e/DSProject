import string
import random

def suurväike(sõne):
    muudetud_sõne = ""
    märk = random.choice(string.punctuation)
    for täht in sõne:
        if täht in string.punctuation:
            täht = märk
            muudetud_sõne += täht
        elif täht == täht.upper() or täht.lower():
            täht = täht.swapcase()
            muudetud_sõne += täht
        
    return(muudetud_sõne)

sõne = input("Sisesta sõne: ")
suurväike(sõne)
print (suurväike(sõne))
