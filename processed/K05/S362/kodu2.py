import string
import random

def suurväike(sõne):
#     sõne=input("Sisesta oma lause: ")
    sõned=""
    suvaline_kirjavahemärk=random.choice(string.punctuation) #choice() asemel saab ka uus_märk=string.punctuation[randrange(0,len(string.punctuation))] kasutada
    for tähti in sõne:
        if tähti.isupper():
            tähti=tähti.lower()
        elif tähti.islower():
            tähti=tähti.upper()
        elif tähti in string.punctuation:
            
            tähti=tähti.replace(tähti,suvaline_kirjavahemärk)
        sõned=sõned+tähti
    return sõned
sõne="leoPARD! Kus sa oled? Tipp-Topp!"
print(suurväike(sõne))
    

    
    
