#suured väikeseks ja väiksed suureks
import string
import random


lower = string.ascii_lowercase
upper = string.ascii_uppercase
punctuation = string.punctuation


def suurväike(arg):
    alg_lause = list(arg)
    lause = []
    kordaja = random.randint(0,30)
    for char in alg_lause:
        
        if char == ' ':
            char = ' '
            lause.append(char)
            
        elif char in lower:
            char = char.upper()
            lause.append(char)
            
        elif char in upper:
            char = char.lower()
            lause.append(char)
            
        elif char in punctuation:
            char = punctuation[kordaja]
            lause.append(char)
            
        else:
            lause.append(char)
            
            
    prinditav = ''.join(map(str, lause))
    return prinditav
            
            
suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut.")