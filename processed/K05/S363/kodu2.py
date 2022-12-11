import string
import random

def suurväike(sõna):
    märgid = string.punctuation
    märk = random.choice(märgid)
    uus = ""
    for i in sõna:
        if i.isupper() == True:
            i = i.lower()
            
        elif i.islower() == True:
            i = i.upper()
            
        elif i in märgid:
            i = märk
            
        uus = uus + i
            
    return uus