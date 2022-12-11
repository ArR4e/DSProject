import random
import string

def suurväike(sõne):
    swapped = []
    punctuation_list = list(string.punctuation)
    random.shuffle(punctuation_list)
    rnd_punctsymbol = punctuation_list[0]
    for char in sõne:
        if char in string.punctuation:
            swapped.append(rnd_punctsymbol)
        elif char.isupper():
            swapped.append(char.islower())
        elif char.islower():
            swapped.append(char.isupper())
        else:
            swapped.append(char)
            
    return ''.join(swapped)

sisu = input("Sisestage sõne: ")
suurväike(sisu)  
        
        

        