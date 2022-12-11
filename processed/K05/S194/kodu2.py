import string     # oli ülesannetelehel mainimata
from random import randint

def suurväike(s):
    vahetus0 = s.swapcase()
    for p in vahetus0:
        if p in string.punctuation:
            suvalisesymboli_indeks = randint(0, len(string.punctuation)-1)
            uusp = p.replace(p, string.punctuation[suvalisesymboli_indeks])
            vahetus1 =  vahetus0.replace(p, uusp)
    return vahetus1

print(suurväike("p,P,!!"))