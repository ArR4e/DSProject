import string
from random import randint

def suurväike(x):
    rng_char = string.punctuation[randint(0, len(string.punctuation) - 1)]
    swapped = []
    i = 0
    
    for char in x:
        if char.isupper():
            swapped.append(char.lower())
        elif char.islower():
            swapped.append(char.upper())
        elif char in string.punctuation:
            swapped.append(rng_char)
        else:
            swapped.append(char)
    
    swap_str = ''
    return swap_str.join(swapped)
            

