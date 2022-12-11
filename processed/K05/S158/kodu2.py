import random
import string
sõne = input("Kirjuta midagi: ")
def suurväike(sõne) :
    uus = ""
    for n in sõne:
        if n.isupper() or n.islower():
            uus += n.swapcase()
        elif n in string.punctuation:
            uus += random.choice(string.punctuation)
    return uus
print(suurväike(sõne))