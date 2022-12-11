from random import randint
def minu_shuffle(järjend):
    elementide_arv = len(järjend)
    for i in range(0, elementide_arv):
        suvaline_indeks = randint(0, elementide_arv-1)
        järjend[i], järjend[suvaline_indeks] = järjend[suvaline_indeks], järjend[i]

        
    