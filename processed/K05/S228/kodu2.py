import string
import random

def suurväike(sõne):
    uus_sõne = ""
    suvaline_vahemärk = random.choice(string.punctuation)
    for i in sõne:
        if i.islower():
            uus_sõne = uus_sõne + i.upper()
        elif i.isupper():
            i.lower()
            uus_sõne = uus_sõne + i.lower()
        elif i.isspace():
            uus_sõne = uus_sõne + i
            continue
        elif i == "":
            break
        else:
            uus_sõne = uus_sõne + suvaline_vahemärk
    return uus_sõne

tekst = input("Sisesta sõna või lause: ")
print(suurväike(tekst))