import string
import random
def suurväike(sõne):
    n=random.randint(1, 35)
    uussõne=""
    for i in range (len(sõne)):
        if sõne[i].isupper():
            uussõne+= sõne[i].lower()
        elif sõne[i].islower():
            uussõne+= sõne[i].upper()
        elif sõne[i] in string.punctuation:
            uussõne+= string.punctuation[n]
        elif sõne[i] == " ":
            uussõne+= " "
    return uussõne
suurväike("Erakordselt vahva, mu kallid sõbrad & tuttavad!!")