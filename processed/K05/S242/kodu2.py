import string
import random

def suurväike2(sõna):
    for täht in sõna:
        if täht.islower():
            täht = täht.upper()
        elif täht.isupper():
            täht = täht.lower()
        elif täht in string.punctuation:
            täht = random.choice(string.punctuation)
        print(' '.join (täht.strip()))
            
            
def suurväike(sõna):
    sõna = sõna.swapcase()
    sõna.find(string.punctuation)
    for täht in sõna:
        if täht in string.punctuation:
            täht = random.choice(string.punctuation)
    if sõna in string.punctuation == True:
        sõna.find(string.punctuation)
    return sõna


