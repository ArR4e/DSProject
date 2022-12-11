import string
import random
def suurväike(sõne):
    sõne2=""
    suvaline=random.choice(string.punctuation)
    for i in sõne:
        if i.islower():
            sõne2+=i.upper()
        elif i.isupper():
            sõne2+=i.lower()
        elif i.isspace():
            sõne2+=" "
        elif i in string.punctuation:
            sõne2+=suvaline
    return(sõne2)
suurväike("Tere, madis, kalle!")