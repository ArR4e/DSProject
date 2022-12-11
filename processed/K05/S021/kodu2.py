import string
import random
def suurväike(a):
    tähed = a.swapcase()
    asendus = random.choice(string.punctuation)
    lõplik = tähed
    for x in tähed:
        if x in string.punctuation:
            lõplik = lõplik.replace(x, asendus)
    return lõplik 
    
muudetud=suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut.")
print(muudetud)
    
    
    