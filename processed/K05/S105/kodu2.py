import string
import random

def suurväike(a):
    uus=""
    
    for i in string.punctuation:
        if random.randint(0,5) == 3:
            suva=i
            break
        else:
            continue
          
    for char in a:
        if char.isupper()==True:
            uus=uus+char.lower()
        elif char.islower()==True:
            uus=uus+char.upper()
        elif char in string.punctuation:
            uus=uus+suva
        else:
            uus=uus+char
    
    return uus