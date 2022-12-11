import string
from random import randint
def suurväike(sõne):
    i=0
    suvaline_indeks=randint(0, 31)
    tulemus=string.punctuation
    tulemus2=tulemus[suvaline_indeks]
    muudetud_sõne=sõne.swapcase()
    while i<32:
        muudetud_sõne=muudetud_sõne.replace(tulemus[i], tulemus2)
        i+=1
    return muudetud_sõne