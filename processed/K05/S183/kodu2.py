import string
import random

def suurväike(sõna):
    jah = ""
    sama = random.randint(0,31)
    for i in sõna:
        if i in string.punctuation:
            jah += string.punctuation[sama]
        elif i == i.upper():
            jah += i.lower()
        elif i in i.lower():
            jah += i.upper()
    return(jah)
