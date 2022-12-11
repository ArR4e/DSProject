import random
import string

def suurväike(sõne):
    uus_sõne = ""
    sümbolid = random.choice(string.punctuation)
    while True:
        for i in range(len(sõne)):
            if sõne[i].isupper():
                uus_sõne += sõne[i].lower()
            elif sõne[i].islower():
                uus_sõne += sõne[i].upper()
            elif sõne[i] == " ":
                uus_sõne += sõne[i]
            else:
                for a in string.punctuation:
                    uus_sõne += sõne[i].replace(sõne[i], sümbolid)
                    break
        return uus_sõne
    
print(suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut."))