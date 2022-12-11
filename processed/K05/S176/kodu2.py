import string
import random

def suurväike(sõne):
    uus_sõne = ""
    for täht in sõne:
        if täht.isupper():
            uus_sõne += täht.lower()
        elif täht.islower():
            uus_sõne += täht.upper()
        elif täht in string.punctuation:
            uus_sõne += random.choice(string.punctuation)
        else:
            uus_sõne += " "
    print(uus_sõne)