import random
import string

lause=input("Kirjuta mõni lause: ")

def suurväike(lause):
    uus_lause = ""
    sümbol = random.choice(string.punctuation)
    for i in lause:
        if i.isupper():
            uus_lause = uus_lause + i.lower()
        elif i.islower():
            uus_lause = uus_lause + i.upper()
        elif i == " ":
            uus_lause = uus_lause + i
        elif i in string.punctuation:
            uus_lause = uus_lause + sümbol            
    return uus_lause
    