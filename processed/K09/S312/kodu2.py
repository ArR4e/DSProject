from random import randint

def minu_shuffle(järjend):
    pikkus = len(järjend)
    for el in järjend:
        juhuslik = randint(0,pikkus-1)
        elenedi_indeks = järjend.index(el) 
        järjend[elenedi_indeks], järjend[juhuslik] = järjend[juhuslik], järjend[elenedi_indeks]