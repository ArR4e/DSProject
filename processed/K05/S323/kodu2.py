import string
import random

sõne = input("Sisestage sõne: ")

def suurväike(sõne):
    #juhuslikult valitud sümbol mis asendab kõik sõnes leiduvad sümbolid peale tühiku
    sümbol = random.choice(string.punctuation)
    uus_sõne = ""
    for i in range (len(sõne)):
        if sõne[i].isupper():
            uus_sõne += sõne[i].lower()
        elif sõne[i].islower():
            uus_sõne += sõne[i].upper()
        elif sõne[i] == " ":
            uus_sõne += " "
        elif sõne[i] in string.punctuation:
            uus_sõne += sümbol
    return(uus_sõne)

print(suurväike(sõne))