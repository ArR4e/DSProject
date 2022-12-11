from random import randint
from string import punctuation
sone = input("Sisestage midagi: ")

def suurväike(sone):
    s1 = sone.swapcase()
    m = punctuation[randint(0, 31)]
    for i in sone:
        if i in punctuation:
            sone = sone.replace(i, m)
    print(s1)

    
suurväike(sone)