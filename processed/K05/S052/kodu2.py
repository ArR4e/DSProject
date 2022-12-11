import string
import random

tekst = input("Sisesta tekst: ")

def suurväike(tekst):
    
    result = string.punctuation
    pikkus = len(result)
    skoop = random.randint(1, pikkus - 1)
    vahemark = result[skoop]
    for character in tekst:
        if character == ' ':
            pass
        else:
            if not character.isalpha():
                if not character.isdigit():
                    tekst = tekst.replace(character, vahemark)
    return tekst.swapcase()


suurväike(tekst)
tekst = suurväike(tekst)
print(tekst)