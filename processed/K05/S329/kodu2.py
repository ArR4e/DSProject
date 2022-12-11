import random
import string

def suurväike(a):
    swapped = []
    punctuation_list = list(string.punctuation)
    random.shuffle(punctuation_list)
    rnd_punctsymbol = punctuation_list[0]
    for char in a:
        if char in string.punctuation:
            swapped.append(rnd_punctsymbol)
        elif char.islower():
            swapped.append(char.upper())
        elif char.isupper():
            swapped.append(char.lower())
        else:
            swapped.append(char)
    
    return ''.join(swapped)


tekst = input("Palun kirjutage teksti: ")

print(suurväike(tekst))
