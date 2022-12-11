import string
import random

def suurväike(midagi):
    sone = ''
    vahemark = random.choice(string.punctuation)
    for i in midagi:
        if i in string.punctuation:
            sone += vahemark
        elif i.islower():
            a = i.upper()
            sone += a
        elif i.isupper:
            a = i.lower()
            sone += a

    return sone
            
print(suurväike('!!Mina olen tubli!!!!'))