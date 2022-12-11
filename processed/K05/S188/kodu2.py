import random
import string

def suurväike(sõna):
    i = 0
    uus_sõna = ""
    sümbol = random.choice(string.punctuation)
    while i < len(sõna):
        liige = sõna[i]
        if liige.isupper():
            uus_sõna += liige.lower()
        elif liige.islower():
            uus_sõna += liige.upper()
        elif liige == " ":
            uus_sõna += " "
        else:
            uus_sõna += sümbol
        i += 1        
    return(uus_sõna)
