from random import randint
import string

def suurväike(sõne):
    s = sõne.swapcase()
    kirjavahemärk = string.punctuation[randint(0,len(string.punctuation)-1)]
    for char in string.punctuation:
        s = s.replace(char,kirjavahemärk)
    return s

print(suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut."))