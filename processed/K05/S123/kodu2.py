import string
import random

def suurväike(sõne):
    r=random.randint(1, 35)
    uus=""
    for i in range(len(sõne)):
        if sõne[i].isalpha():
            uus+=sõne[i].swapcase()
        elif sõne[i] in string.punctuation:
            uus+=string.punctuation[r]
        elif sõne [i] == " ":
            uus+= " "
    return uus
    
    
sisend=input("Kirjuta sõne:")
suurväike(sisend)
