import random
import string

sõne = input("Sisesta sõne: ")

def suurväike(sõne):
    uus_sõna = ""
    for i in sõne:
        if i in string.punctuation:
            uus_sõna += i.replace(i, random.choice(string.punctuation)).rstrip()
        else:
            if i.isupper():
                uus_sõna += (i.lower())
            else:
                uus_sõna += (i.upper())  
    return uus_sõna

uus_sõna = suurväike(sõne)

print(uus_sõna)
    


    
    