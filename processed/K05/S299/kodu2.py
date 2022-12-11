import string
import random

def suurväike(x):
    uus=''
    b=random.choice(string.punctuation)
    for a in x:
        if (a.isupper())==True:
            uus+=(a.lower())
        if (a.islower())==True:
            uus+=(a.upper())
        if (a.isspace())==True:
            uus+=a
        if a in string.punctuation:
            uus+=b
    return uus      
    
