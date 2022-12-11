import string
import random

def suurväike(x):
    uus = ''
    s = string.punctuation
    juhuslik = random.choice(s)
    for a in x:
        if a.isupper() == True:
            uus += (a.lower())
            
            
        elif a.islower() == True:
            uus += (a.upper())
            
        elif a.isspace() == True:
            uus += a
        
        elif a != s:
            uus += juhuslik
    return uus