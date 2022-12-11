import string
import random

sõne = input("Sisesta mingi sõne: ")
def suurväike(sõne):
    uus_sõna = ''
    uus3 = random.choice(string.punctuation)
    for char in sõne:
        if char.isupper() == True:
            uus1 = char.swapcase()
            uus_sõna += uus1
        elif char.islower() == True:
            uus2 = char.swapcase()
            uus_sõna += uus2
        elif char == ' ':
            uus_sõna += ' '
        elif char in string.punctuation:
            uus_sõna += uus3
    return uus_sõna
suurväike(sõne)
