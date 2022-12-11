import random
import string
def suurväike(sõne):
    i = 0
    uus_sõne = ""
    valik = string.punctuation
    while i < len(sõne):
        if sõne[i].islower():
            uus_sõne = uus_sõne + sõne[i].upper() 
        else:
            if sõne[i].isupper():
                uus_sõne = uus_sõne + sõne[i].lower()
            else:
                if sõne[i] == " ":
                    uus_sõne = uus_sõne + " "
                else:
                     if sõne.isalpha() != True:
                        uus_sõne = uus_sõne + random.choice(valik)
        i = i + 1
                
    print(uus_sõne)
sisestus = input("Sisesta sõne: ")
suurväike(sisestus)