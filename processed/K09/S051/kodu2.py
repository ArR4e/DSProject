from random import choice

def minu_shuffle(järjend):
    indeksite_järjend = []
    koopia = järjend.copy()
    for i in range(len(järjend)):
        indeksite_järjend.append(i)
        järjend.pop(0)
    
    while indeksite_järjend != []:
        indeks = choice(indeksite_järjend)
        järjend.append(koopia[indeks])
        indeksite_järjend.remove(indeks)