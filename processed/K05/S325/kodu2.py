import string
from random import *
def suurväike(s):
    l=str("")
    symb=choice(string.punctuation)
    for char in s:
        if char.islower() == True:
            char = char.upper()
        elif char.isupper() == True:
            char = char.lower()
        else:
            char=symb
        l+=char
    return(l)