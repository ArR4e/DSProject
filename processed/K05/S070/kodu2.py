import string
import random
def suurväike(sõna):
    sümbol = string.punctuation[random.randint(1, 32)]
    lõplik = ""
    for k in sõna:
        if k.islower():
            #print(k.upper(), end ="")
            lõplik += k.upper()
        if k.isupper():
            #print(k.lower(), end ="")
            lõplik += k.lower()
        if k in string.punctuation:
            #print(sümbol, end ="")
            lõplik += sümbol
        elif not k.islower() and not k.isupper() and k not in string.punctuation:
            lõplik += k
            
    return lõplik

