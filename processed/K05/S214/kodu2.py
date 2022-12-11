import random
import string

def suurväike(sõne):
    a = random.choice(string.punctuation)
    väljund =""
    for i in sõne:
        if i.isupper():
            väljund+=str(i.lower())
        elif i.islower():
            väljund+=str(i.upper())
        elif i ==" ":
            väljund+=str(i)
        else:
            i = a
            väljund+=str(i)
    return väljund