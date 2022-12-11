import string
import random

def suurväike(el):
    if el.isupper() == True:
        return(el.lower())
    elif el.islower()==True:
        return(el.upper())
    elif el in string.punctuation:
        el=string.punctuation
        el=(''.join(random.choice(el)))
        return(el)
    elif el==" ":
        return(el)
            

sone= input("Sisesta sõne: ")
for el in sone:
    suurväike(el)